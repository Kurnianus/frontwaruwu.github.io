# Generated by Django 4.1.7 on 2023-04-18 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_user_name_admin_nama'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='Nama',
            new_name='user_name',
        ),
    ]
