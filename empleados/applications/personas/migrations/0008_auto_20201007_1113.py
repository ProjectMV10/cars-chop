# Generated by Django 2.2.7 on 2020-10-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0007_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
