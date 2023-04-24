# Generated by Django 4.2 on 2023-04-17 13:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("bitches", "0003_remove_bitch_image_alter_bitch_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bitch",
            name="id",
            field=models.UUIDField(
                db_index=True,
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.UUIDField(
                db_index=True,
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="id",
            field=models.UUIDField(
                db_index=True,
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
