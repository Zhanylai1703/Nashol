# Generated by Django 4.2 on 2023-04-17 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
        ("bitches", "0002_alter_bitch_options_alter_bitch_image_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bitch",
            name="image",
        ),
        migrations.AlterField(
            model_name="bitch",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bitches",
                to="users.user",
                verbose_name="автор",
            ),
        ),
        migrations.AlterField(
            model_name="bitch",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bitches",
                to="bitches.category",
                verbose_name="категория",
            ),
        ),
        migrations.AlterField(
            model_name="bitch",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="цена"
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="bitch",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="bitches.bitch",
                verbose_name="Пост",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="is_preview",
            field=models.BooleanField(default=False, verbose_name="Превью"),
        ),
        migrations.AlterField(
            model_name="image",
            name="photo",
            field=models.FileField(upload_to="images/%Y/%m/%d/", verbose_name="Фото"),
        ),
    ]
