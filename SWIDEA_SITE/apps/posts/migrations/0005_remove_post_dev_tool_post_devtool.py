# Generated by Django 5.0.1 on 2024-07-17 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devTools', '0001_initial'),
        ('posts', '0004_remove_post_devtool_post_dev_tool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dev_tool',
        ),
        migrations.AddField(
            model_name='post',
            name='devtool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devTools.devtool', verbose_name='예상 개발툴'),
        ),
    ]
