# Generated by Django 4.2.5 on 2023-09-25 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dws_site', '0008_rename_product_id_product_product_art'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(verbose_name='название организации')),
                ('company_tax_id', models.IntegerField(verbose_name='УНП')),
                ('legal_adress', models.TextField(verbose_name='юридический адрес')),
                ('post_adress', models.TextField(verbose_name='юридический адрес')),
                ('company_email', models.EmailField(max_length=254, verbose_name='эл адрес')),
                ('delivery_adress', models.TextField(verbose_name='адрес доставки')),
                ('position', models.CharField(verbose_name='должность для договора')),
                ('position_name', models.CharField(verbose_name='ФИО для договора')),
                ('bank_details', models.CharField(verbose_name='банковские реквизиты')),
                ('comments', models.TextField(verbose_name='комментарии к заказу')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='цена')),
                ('quantity', models.IntegerField(verbose_name='количество')),
                ('total_sum', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='общая стоимость')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.order', verbose_name='заказ')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='dws_site.product', verbose_name='товар')),
            ],
        ),
    ]