# Generated by Django 2.2.6 on 2019-11-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0003_auto_20191115_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='total_venta',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
