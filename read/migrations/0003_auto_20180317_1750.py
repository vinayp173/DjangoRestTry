# Generated by Django 2.0.1 on 2018-03-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0002_auto_20180317_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
