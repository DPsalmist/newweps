# Generated by Django 4.1.3 on 2022-11-27 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0003_remove_club_club_time_club_meeting_day_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="club",
            name="meeting_time",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
