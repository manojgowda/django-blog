# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cpuandmemeory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twittercount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetcount', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
