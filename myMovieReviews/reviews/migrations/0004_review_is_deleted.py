# Generated by Django 5.0.7 on 2024-07-12 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_review_imgfile_review_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
