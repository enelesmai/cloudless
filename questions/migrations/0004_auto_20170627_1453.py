# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20170627_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Status'),
        ),
    ]
