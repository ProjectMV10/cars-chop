# Generated by Django 2.2.7 on 2020-10-19 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0011_auto_20201019_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_libro', to='personas.CategoriaLibro'),
        ),
    ]
