# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorcycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('pics', models.CharField(max_length=1000)),
            ],
        ),
    ]
