# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-30 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djcelery', '0001_initial'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
                ('runtime', models.FloatField(help_text='in seconds if task succeeded', null=True, verbose_name='运行时间')),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.File', verbose_name='导入文件')),
                ('taskmeta', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='djcelery.TaskMeta')),
            ],
        ),
        migrations.CreateModel(
            name='SqlModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_sql', models.TextField(max_length=255)),
                ('query_sql', models.TextField(max_length=255)),
                ('export_sql', models.TextField(max_length=255)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
    ]
