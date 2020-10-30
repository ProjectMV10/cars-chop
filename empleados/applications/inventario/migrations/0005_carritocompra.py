# Generated by Django 2.2.7 on 2020-10-09 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventario', '0004_auto_20201007_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprado', models.BooleanField(default=False, verbose_name='Comprado')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_carrito', to='inventario.Producto')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_carrito', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]