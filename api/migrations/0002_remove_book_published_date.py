# Generated by Django 5.1.6 on 2025-04-18 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
    ]
