# Generated by Django 4.1.7 on 2023-05-25 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_penghuni_kodeadminpenghuni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kamarkost',
            name='TipeKamar',
            field=models.CharField(choices=[('premium', 'Premium'), ('standard', 'Standard')], max_length=10, null=True),
        ),
    ]
