# Generated by Django 5.0.7 on 2024-07-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('release', models.CharField(max_length=30)),
                ('director', models.TextField()),
                ('actor', models.TextField()),
                ('genre', models.TextField()),
                ('score', models.TextField()),
                ('running_time', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]
