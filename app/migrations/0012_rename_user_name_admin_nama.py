# Generated by Django 4.1.7 on 2023-04-18 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_nama_admin_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='user_name',
            new_name='Nama',
        ),
    ]
