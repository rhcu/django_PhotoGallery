# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photohost', '0005_auto_20161228_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photohost.Album'),
        ),
    ]
