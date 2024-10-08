# Generated by Django 5.0.7 on 2024-10-08 14:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Parent", "0001_initial"),
        ("Student", "0001_initial"),
        ("Teacher", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="leave",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Student.student"
            ),
        ),
        migrations.AddField(
            model_name="parent",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="leave",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Parent.parent"
            ),
        ),
        migrations.AddField(
            model_name="writemsg",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Parent.parent",
                verbose_name="Sender Parent",
            ),
        ),
        migrations.AddField(
            model_name="writemsg",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Student.student",
                verbose_name="Student Involved",
            ),
        ),
        migrations.AddField(
            model_name="writemsg",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Teacher.teacher",
                verbose_name="Recipient Teacher",
            ),
        ),
        migrations.AddIndex(
            model_name="parent",
            index=models.Index(fields=["user"], name="parent_user_id_4cc29e_idx"),
        ),
        migrations.AddConstraint(
            model_name="parent",
            constraint=models.UniqueConstraint(
                fields=("phone_number",), name="unique_contact_number"
            ),
        ),
    ]
