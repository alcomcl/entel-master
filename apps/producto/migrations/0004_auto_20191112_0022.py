# Generated by Django 2.2.6 on 2019-11-12 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_auto_20191112_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='img',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
