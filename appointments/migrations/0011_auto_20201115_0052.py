# Generated by Django 3.1.3 on 2020-11-15 03:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0010_appointment_medic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='medic',
            field=models.ForeignKey(limit_choices_to=models.Q(groups__name='GroupName'), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
