# Generated by Django 3.2.16 on 2022-10-24 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='fname',
            new_name='uname',
        ),
        migrations.RemoveField(
            model_name='users',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='users',
            name='lname',
        ),
    ]