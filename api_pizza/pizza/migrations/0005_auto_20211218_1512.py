# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2021-12-18 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_auto_20211218_1236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={},
        ),
        migrations.AlterField(
            model_name='pizza',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]