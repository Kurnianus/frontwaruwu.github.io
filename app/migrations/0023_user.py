# Generated by Django 4.1.7 on 2023-04-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('userid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
