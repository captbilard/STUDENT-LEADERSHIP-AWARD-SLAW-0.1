# Generated by Django 2.2.7 on 2019-12-04 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slaw', '0002_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nominees',
            name='Level',
            field=models.IntegerField(choices=[(100, '100'), (200, '200'), (300, '300'), (400, '400'), (500, '500'), (600, '600'), (700, '700')], default='100L'),
        ),
    ]
