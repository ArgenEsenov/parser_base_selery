# Generated by Django 4.1.3 on 2022-12-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_ads_image_remove_image_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='image_url',
        ),
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылки Изображения'),
        ),
    ]