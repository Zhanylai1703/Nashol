# Generated by Django 4.2 on 2023-04-24 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_rename_typee_user_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
