# Generated by Django 4.2.5 on 2023-09-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dws',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(verbose_name='название двигателя')),
                ('goods_id', models.IntegerField(verbose_name='артикул')),
                ('manufacturer', models.CharField(verbose_name='производитель')),
                ('transport_model', models.CharField(verbose_name='применяемость')),
                ('category', models.CharField(verbose_name='категория')),
                ('price', models.FloatField(verbose_name='цена')),
                ('image', models.ImageField(upload_to='', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'двигатель',
                'verbose_name_plural': 'двигатели',
            },
        ),
    ]
