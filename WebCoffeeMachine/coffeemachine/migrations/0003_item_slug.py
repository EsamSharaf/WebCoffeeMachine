# Generated by Django 4.2.13 on 2024-06-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeemachine', '0002_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
