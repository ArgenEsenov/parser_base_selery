# Generated by Django 4.1.3 on 2022-12-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_catygory_ads_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='phone',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
