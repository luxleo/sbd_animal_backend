# Generated by Django 4.1.5 on 2023-01-27 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sbd_animal.work_out.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
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
                    "max_1rm",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=5,
                        validators=[sbd_animal.work_out.models.positive_validator],
                    ),
                ),
                (
                    "total_cal",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=5,
                        validators=[sbd_animal.work_out.models.positive_validator],
                    ),
                ),
                (
                    "total_lift",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=5,
                        validators=[sbd_animal.work_out.models.positive_validator],
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "body_weight",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=4,
                        validators=[sbd_animal.work_out.models.body_weight_validator],
                    ),
                ),
                (
                    "athlete",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="WorkoutType",
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
                ("name", models.CharField(max_length=30)),
                (
                    "workout_distance",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=3,
                        validators=[sbd_animal.work_out.models.positive_validator],
                    ),
                ),
                ("category", models.CharField(blank=True, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name="WorkoutRangePreference",
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
                    "custom_range",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=5,
                        validators=[sbd_animal.work_out.models.positive_validator],
                    ),
                ),
                (
                    "athlete",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "workout_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="work_out.workouttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rep",
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
                ("rep_order_number", models.PositiveSmallIntegerField()),
                (
                    "calorie",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=5,
                        validators=[sbd_animal.work_out.models.positive_validator],
                    ),
                ),
                (
                    "workout_weight",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=5,
                        validators=[sbd_animal.work_out.models.positive_validator],
                    ),
                ),
                ("reps", models.PositiveSmallIntegerField()),
                (
                    "log",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="work_out.log"
                    ),
                ),
            ],
            options={
                "ordering": ["rep_order_number"],
            },
        ),
        migrations.AddField(
            model_name="log",
            name="workout_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="work_out.workouttype"
            ),
        ),
    ]
