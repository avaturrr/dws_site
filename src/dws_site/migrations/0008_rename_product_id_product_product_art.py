# Generated by Django 4.2.5 on 2023-09-24 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dws_site', '0007_alter_product_options_alter_product_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_id',
            new_name='product_art',
        ),
    ]
