# Generated by Django 3.2.6 on 2024-03-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0016_alter_detalleventa_id_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='fecha_cobro',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
