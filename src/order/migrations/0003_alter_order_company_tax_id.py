# Generated by Django 4.2.5 on 2023-09-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='company_tax_id',
            field=models.CharField(verbose_name='УНП'),
        ),
    ]