# Generated by Django 5.0.7 on 2024-10-08 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Leave",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "leave_type",
                    models.CharField(
                        choices=[
                            ("SICK", "Sick Leave"),
                            ("CASUAL", "Casual Leave"),
                            ("EMERGENCY", "Emergency Leave"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("APPROVED", "Approved"),
                            ("REJECTED", "Rejected"),
                        ],
                        default="PENDING",
                        max_length=20,
                    ),
                ),
                ("leave_description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Parent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Contact number should be 9 digits.",
                                regex="^\\d{9}$",
                            )
                        ],
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female")],
                        default="M",
                        max_length=1,
                        null=True,
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name_plural": "Parent",
                "db_table": "parent",
            },
        ),
        migrations.CreateModel(
            name="WriteMsg",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text_msg", models.TextField(verbose_name="Message Text")),
                (
                    "response",
                    models.TextField(
                        blank=True, null=True, verbose_name="Teacher Response"
                    ),
                ),
            ],
        ),
    ]
