# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-07-03 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_item_in_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('house_no', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=8)),
            ],
        ),
    ]