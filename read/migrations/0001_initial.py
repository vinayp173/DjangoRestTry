# Generated by Django 2.0.1 on 2018-03-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(default='', max_length=10)),
                ('password', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
