# Generated by Django 4.1.3 on 2022-11-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0002_alter_club_instructor"),
    ]

    operations = [
        migrations.RemoveField(model_name="club", name="club_time",),
        migrations.AddField(
            model_name="club",
            name="meeting_day",
            field=models.CharField(
                choices=[
                    ("Monday", "Monday"),
                    ("Tuesday", "Tuesday"),
                    ("Wednesday", "Wednesday"),
                    ("Thursday", "Thursday"),
                    ("Friday", "Friday"),
                    ("Saturday", "Saturday"),
                ],
                default="Saturday",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="club",
            name="meeting_time",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
