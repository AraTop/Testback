# Generated by Django 5.0.1 on 2024-02-06 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_menu_path_menu_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='url',
        ),
    ]
