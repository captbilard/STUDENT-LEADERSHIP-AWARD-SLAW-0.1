# Generated by Django 3.1.1 on 2020-09-19 13:31

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('C360N', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteers',
            name='Country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='volunteers',
            name='Phone_Number',
            field=models.IntegerField(),
        ),
    ]
