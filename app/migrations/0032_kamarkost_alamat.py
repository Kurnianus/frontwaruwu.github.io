# Generated by Django 4.1.7 on 2023-05-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_admin_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='kamarkost',
            name='alamat',
            field=models.URLField(default='https://maps.google.com'),
        ),
    ]
