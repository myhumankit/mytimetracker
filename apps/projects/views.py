from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from projects.models import Activity, Capacity, Leave, Project, Resource


class ProjectListView(LoginRequiredMixin, ListView):

    model = Project
    template_name = "projects/project_list.html"


class ProjectDetailView(LoginRequiredMixin, ListView):

    model = Project
    template_name = "projects/project_detail.html"

    def get_queryset(self):
        queryset = get_object_or_404(Project, id=self.kwargs["pk"]).get_descendants(
            include_self=True
        )
        return queryset


class ActivityListView(LoginRequiredMixin, ListView):

    model = Activity
    paginate_by = 50

    def get_queryset(self):
        queryset = Activity.objects.filter(user=self.request.user)
        for activity in queryset:
            activity.week = activity.date.isocalendar()[1]
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        start_date = timezone.now().today().date()
        try:
            end_date = Capacity.objects.filter(user=user).order_by("-date")[0].date
        except:
            end_date = start_date
        delta = end_date - start_date

        next_available_date = start_date

        # absences ?

        # temps de travail estimé
        total_load = timedelta()

        projects = {}
        for project in Project.objects.filter(resource__user=user).distinct():
            # qui ?
            # users = CustomUser.objects.filter(resource__project=project).distinct()

            # combien de temps alloué sur le projet ?
            t_user = timedelta()
            for resource in Resource.objects.filter(project=project, user=user):
                t_user += resource.duration

            # quel rapport ?
            t_total = project.allotted_time
            if t_total == 0:
                r = 1
            else:
                r = t_user / t_total

            load = r * project.remaining_time_needed
            total_load += load
            projects[project.title] = load

        context["total_load"] = total_load

        date_list = []
        capacity_list = []
        booked_list = []
        available_list = []
        leave_list = []
        day_number = delta.days + 1
        for i in range(day_number):
            date = start_date + timedelta(days=i)

            # temps disponible
            capacity = timedelta()
            capacities = Capacity.objects.filter(user=user, date=date)
            for c in capacities:
                capacity += c.duration

            # temps déjà attribué
            booked = timedelta()
            resources = Resource.objects.filter(user=user, date=date)
            for resource in resources:
                booked += resource.duration

            # y-a-t-il des congés ?
            leave = timedelta()
            leaves = Leave.objects.filter(user=user, date=date)
            for l in leaves:
                leave += l.duration

            # atribution du temps
            available = capacity - booked - leave

            if available > timedelta() and total_load > timedelta():
                if (total_load - available) > timedelta():
                    total_load -= available
                    available = timedelta()
                else:
                    available -= total_load
                    total_load = timedelta()
                    next_available_date = date

            date_list.append(date)
            capacity_list.append(capacity)
            booked_list.append(booked)
            leave_list.append(leave)
            available_list.append(available)

        context["start_date"] = start_date
        context["end_date"] = end_date
        context["delta"] = day_number
        context["date_list"] = date_list
        context["capacity_list"] = capacity_list
        context["booked_list"] = booked_list
        context["leave_list"] = leave_list
        context["available_list"] = available_list
        context["project_list"] = projects
        context["next_available_date"] = next_available_date
        return context


class LeaveListView(LoginRequiredMixin, ListView):

    model = Leave

    def get_queryset(self):
        queryset = Leave.objects.filter(user=self.request.user)
        return queryset
