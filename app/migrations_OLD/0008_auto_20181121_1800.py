# Generated by Django 2.1.1 on 2018-11-21 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181121_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='Due_dates',
        ),
        migrations.AddField(
            model_name='admin',
            name='Due_dates1',
            field=models.DateField(default=1986),
            preserve_default=False,
        ),
    ]