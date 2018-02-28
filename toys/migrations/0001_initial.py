# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-28 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=150)),
                ('description', models.CharField(blank=True, default='', max_length=250)),
                ('toy_category', models.CharField(default='', max_length=200)),
                ('release_date', models.DateTimeField()),
                ('was_included_in_home', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
