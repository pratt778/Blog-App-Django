# Generated by Django 5.0.3 on 2024-05-20 12:15

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
