# Generated by Django 4.2 on 2023-04-18 13:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_managers_user_date_joined_user_email_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="typee",
            new_name="type",
        ),
    ]
