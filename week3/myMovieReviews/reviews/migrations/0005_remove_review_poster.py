# Generated by Django 5.0.7 on 2024-07-12 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='poster',
        ),
    ]
