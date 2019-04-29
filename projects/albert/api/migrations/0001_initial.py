# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('cover', models.IntegerField()),
                ('isbn', models.IntegerField()),
            ],
        ),
    ]