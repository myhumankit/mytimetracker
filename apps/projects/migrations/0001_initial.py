# Generated by Django 2.2.5 on 2019-09-22 16:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='mise à jour')),
                ('title', models.CharField(max_length=1000, verbose_name='titre')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='commentaire')),
            ],
            options={
                'verbose_name': 'localisation',
                'verbose_name_plural': 'localisations',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='mise à jour')),
                ('title', models.CharField(max_length=1000, verbose_name='titre')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='commentaire')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='projects.Project')),
            ],
            options={
                'verbose_name': 'projet',
                'verbose_name_plural': 'projets',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='mise à jour')),
                ('type', models.CharField(choices=[('C', 'congé payé'), ('R', 'récupération'), ('F', 'jour ferié'), ('M', 'arrêt maladie'), ('S', 'congé sans solde'), ('A', 'autre ...')], default='C', max_length=1, verbose_name="type d'absence")),
                ('date', models.DateField()),
                ('duration', models.DurationField(default=datetime.timedelta(0, 25200), verbose_name='durée')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='commentaire')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='leaves', related_query_name='leave', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'absence',
                'verbose_name_plural': 'absences',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='HistoricalProject',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='création')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='mise à jour')),
                ('title', models.CharField(max_length=1000, verbose_name='titre')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='commentaire')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.Project')),
            ],
            options={
                'verbose_name': 'historical projet',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLocation',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='création')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='mise à jour')),
                ('title', models.CharField(max_length=1000, verbose_name='titre')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='commentaire')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical localisation',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLeave',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='création')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='mise à jour')),
                ('type', models.CharField(choices=[('C', 'congé payé'), ('R', 'récupération'), ('F', 'jour ferié'), ('M', 'arrêt maladie'), ('S', 'congé sans solde'), ('A', 'autre ...')], default='C', max_length=1, verbose_name="type d'absence")),
                ('date', models.DateField()),
                ('duration', models.DurationField(default=datetime.timedelta(0, 25200), verbose_name='durée')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='commentaire')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='leave', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'historical absence',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalActivity',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False, verbose_name='création')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, verbose_name='mise à jour')),
                ('date', models.DateField()),
                ('duration', models.DurationField(default=datetime.timedelta(0, 3600), verbose_name='durée')),
                ('is_teleworking', models.BooleanField(default=False, verbose_name='télétravail')),
                ('is_business_trip', models.BooleanField(default=False, verbose_name='déplacement')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='commentaire')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='activity', to='projects.Location', verbose_name='localisation')),
                ('project', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='activity', to='projects.Project', verbose_name='projet')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='activity', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'historical activité',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='mise à jour')),
                ('date', models.DateField()),
                ('duration', models.DurationField(default=datetime.timedelta(0, 3600), verbose_name='durée')),
                ('is_teleworking', models.BooleanField(default=False, verbose_name='télétravail')),
                ('is_business_trip', models.BooleanField(default=False, verbose_name='déplacement')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True, verbose_name='commentaire')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activities', related_query_name='activity', to='projects.Location', verbose_name='localisation')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activities', related_query_name='activity', to='projects.Project', verbose_name='projet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activities', related_query_name='activity', to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'activité',
                'verbose_name_plural': 'activités',
                'ordering': ('-date',),
            },
        ),
    ]
