# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-12 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20170625_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorcycle',
            name='pics',
            field=models.FileField(upload_to='uploads/pics'),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='report',
            field=models.FileField(upload_to='uploads/reports'),
        ),
    ]
