# Generated by Django 2.2.7 on 2020-10-16 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0010_auto_20201013_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(verbose_name='Precio Producto'),
        ),
    ]