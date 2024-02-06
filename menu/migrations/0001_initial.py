# Generated by Django 5.0.1 on 2024-02-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('path', models.CharField(blank=True, max_length=255)),
                ('menu_name', models.CharField(max_length=255)),
            ],
        ),
    ]
