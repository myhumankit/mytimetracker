# Generated by Django 2.2.5 on 2019-09-27 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='start_balance',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='solde de départ'),
        ),
    ]
