# Generated by Django 2.1.1 on 2018-11-21 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_s_box'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='s_box',
            new_name='submission_box',
        ),
    ]