# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-30 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cevent',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.User'),
        ),
    ]