# Generated by Django 5.0.7 on 2024-07-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_imgfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='imgfile',
        ),
        migrations.AddField(
            model_name='review',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
