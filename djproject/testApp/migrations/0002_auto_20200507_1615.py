# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-07 10:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blorejobs',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='chennaijobs',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='hydjobs',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='punejobs',
            name='phonenumber',
        ),
    ]
