# Generated by Django 4.1.7 on 2023-05-23 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_alter_kamarkost_kodeadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='penghuni',
            name='kodeadminpenghuni',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='app.admin'),
            preserve_default='True',
        ),
    ]
