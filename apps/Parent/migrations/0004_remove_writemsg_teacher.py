# Generated by Django 5.0.7 on 2024-10-12 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Parent", "0003_leave_teacher"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="writemsg",
            name="teacher",
        ),
    ]
