# Generated by Django 4.1.5 on 2023-02-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bulletinBoard", "0003_remove_reply_parent_reply"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reply",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
