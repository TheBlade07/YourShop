# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_item_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='rating',
            field=models.FloatField(default=None),
        ),
    ]
