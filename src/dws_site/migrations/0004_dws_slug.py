# Generated by Django 4.2.5 on 2023-09-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dws_site', '0003_rename_category_dws_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='dws',
            name='slug',
            field=models.SlugField(max_length=225, null=True, unique=True, verbose_name='URL'),
        ),
    ]