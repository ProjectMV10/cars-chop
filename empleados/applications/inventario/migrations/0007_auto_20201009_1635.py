# Generated by Django 2.2.7 on 2020-10-09 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_auto_20201009_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carritocompra',
            name='precio',
            field=models.FloatField(verbose_name='Precio'),
        ),
    ]
