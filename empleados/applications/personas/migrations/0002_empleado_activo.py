# Generated by Django 2.2.7 on 2020-08-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Anulado'),
        ),
    ]
