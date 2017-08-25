# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='FirstName',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='LastName',
            field=models.CharField(max_length=128),
        ),
    ]
