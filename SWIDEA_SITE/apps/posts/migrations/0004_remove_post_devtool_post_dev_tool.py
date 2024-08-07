# Generated by Django 5.0.1 on 2024-07-17 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devTools', '0001_initial'),
        ('posts', '0003_post_devtool_alter_post_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='devtool',
        ),
        migrations.AddField(
            model_name='post',
            name='dev_tool',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='devTools.devtool', verbose_name='개발툴'),
        ),
    ]
