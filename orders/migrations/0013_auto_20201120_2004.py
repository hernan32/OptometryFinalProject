# Generated by Django 3.1.3 on 2020-11-20 23:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0012_auto_20201120_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('LEJ', 'Lejos'), ('CER', 'Cerca')], max_length=3, null=True, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('CRED', 'Tarjeta de Credito'), ('DBTO', 'Tarjeta de Debito'), ('VIRT', 'Billetera Virtual'), ('EFEC', 'Efectivo')], default='EFEC', max_length=4, verbose_name='Metodo de Pago'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='Productos', to='orders.Product', verbose_name='Productos'),
        ),
        migrations.AlterField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(limit_choices_to=models.Q(groups__name='Vendedor'), on_delete=django.db.models.deletion.CASCADE, related_name='Vendedor', to=settings.AUTH_USER_MODEL, verbose_name='Vendedor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='position',
            field=models.CharField(blank=True, choices=[('IZQ', 'Izquierda'), ('DER', 'Derecha')], max_length=3, null=True, verbose_name='Posición'),
        ),
    ]
