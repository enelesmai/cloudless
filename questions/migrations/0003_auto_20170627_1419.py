# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 19:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_project_member_question_image_question_member_question_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='password',
        ),
        migrations.RemoveField(
            model_name='member',
            name='usuario',
        ),
        migrations.AddField(
            model_name='member',
            name='User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
