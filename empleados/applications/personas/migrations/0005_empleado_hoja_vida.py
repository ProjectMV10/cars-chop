# Generated by Django 2.2.7 on 2020-09-08 20:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0004_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default=0.00044004400440044003),
            preserve_default=False,
        ),
    ]
