# Generated by Django 5.0.7 on 2024-10-12 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Teacher", "0008_alter_attendance_unique_together_announcement"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="attendance",
            unique_together=set(),
        ),
    ]
