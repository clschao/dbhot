# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-08-19 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0010_auto_20190819_1545'),
        ('sales', '0004_auto_20190812_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='roles',
            field=models.ManyToManyField(to='rbac.Role'),
        ),
    ]