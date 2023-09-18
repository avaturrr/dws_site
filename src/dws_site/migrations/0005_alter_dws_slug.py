# Generated by Django 4.2.5 on 2023-09-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dws_site', '0004_dws_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dws',
            name='slug',
            field=models.SlugField(max_length=225, unique=True, verbose_name='URL'),
        ),
    ]
