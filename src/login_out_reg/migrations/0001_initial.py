# Generated by Django 4.2.5 on 2023-09-26 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(verbose_name='название организации')),
                ('company_tax_id', models.CharField(verbose_name='УНП')),
                ('legal_adress', models.TextField(verbose_name='юридический адрес')),
                ('post_adress', models.TextField(verbose_name='почтовый адрес')),
                ('company_email', models.EmailField(max_length=254, verbose_name='эл адрес')),
                ('phone_number', models.CharField(null=True, verbose_name='телефон для связи')),
                ('delivery_adress', models.TextField(verbose_name='адрес доставки')),
                ('position', models.CharField(verbose_name='должность для договора')),
                ('position_name', models.CharField(verbose_name='ФИО для договора')),
                ('bank_details', models.CharField(verbose_name='банковские реквизиты')),
                ('comments', models.TextField(verbose_name='комментарии к заказу')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='profils', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]