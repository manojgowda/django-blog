# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160228_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twittercounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=100)),
                ('twittercount', models.IntegerField()),
                ('totalcounts', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Twittercount',
        ),
    ]
