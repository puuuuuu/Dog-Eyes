# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-06 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180806_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storeinfo',
            options={},
        ),
        migrations.AddField(
            model_name='goodstype',
            name='store_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.StoreInfo'),
        ),
    ]
