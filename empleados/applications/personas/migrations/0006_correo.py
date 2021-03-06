# Generated by Django 2.2.7 on 2020-09-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_empleado_hoja_vida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
