# Generated by Django 2.2.6 on 2019-11-12 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='vendedor',
        ),
        migrations.DeleteModel(
            name='Detalle_Venta',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]
