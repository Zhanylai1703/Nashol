# Generated by Django 4.2 on 2023-04-24 11:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_user_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
