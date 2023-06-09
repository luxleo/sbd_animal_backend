# Generated by Django 4.1.5 on 2023-02-01 09:23

from django.db import migrations, models
import sbd_animal.work_out.models


class Migration(migrations.Migration):

    dependencies = [
        ("work_out", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="log",
            name="percentile",
            field=models.DecimalField(
                blank=True,
                decimal_places=1,
                max_digits=4,
                null=True,
                validators=[sbd_animal.work_out.models.positive_validator],
            ),
        ),
    ]
