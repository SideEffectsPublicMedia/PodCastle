# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
