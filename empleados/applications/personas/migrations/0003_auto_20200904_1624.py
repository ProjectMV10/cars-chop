# Generated by Django 2.2.7 on 2020-09-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_empleado_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=100, verbose_name='Habilidad')),
            ],
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['nombres'], 'verbose_name': 'Mis Empleados', 'verbose_name_plural': 'Empleados de la Empresa'},
        ),
        migrations.AlterField(
            model_name='empleado',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
