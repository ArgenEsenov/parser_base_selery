# Generated by Django 4.1.3 on 2022-12-08 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='catygory',
            new_name='category',
        ),
    ]
