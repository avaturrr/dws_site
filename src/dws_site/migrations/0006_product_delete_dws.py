# Generated by Django 4.2.5 on 2023-09-23 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dws_site', '0005_alter_dws_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(verbose_name='название двигателя')),
                ('product_id', models.IntegerField(verbose_name='артикул')),
                ('manufacturer', models.CharField(verbose_name='производитель')),
                ('transport_model', models.CharField(verbose_name='применяемость')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='цена')),
                ('image', models.ImageField(upload_to='', verbose_name='фото')),
                ('slug', models.SlugField(max_length=225, unique=True, verbose_name='URL')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='dws_site.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'двигатель',
                'verbose_name_plural': 'двигатели',
            },
        ),
        migrations.DeleteModel(
            name='Dws',
        ),
    ]
