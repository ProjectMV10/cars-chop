# Generated by Django 2.2.7 on 2020-10-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='acercade',
            field=models.TextField(blank=True, null=True, verbose_name='Acerca del Producto'),
        ),
    ]
