# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-23 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_userinfo_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='deal_date',
            field=models.DateField(null=True),
        ),
    ]
