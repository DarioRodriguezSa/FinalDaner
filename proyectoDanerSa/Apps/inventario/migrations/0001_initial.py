# Generated by Django 3.2.6 on 2023-12-21 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idprducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70)),
                ('existencia', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('precio_compra', models.FloatField()),
                ('estado', models.IntegerField()),
            ],
        ),
    ]
