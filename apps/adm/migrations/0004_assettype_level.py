# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-21 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0003_auto_20181221_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='assettype',
            name='level',
            field=models.CharField(default='', max_length=20, verbose_name='等级'),
        ),
    ]