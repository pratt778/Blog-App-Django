# Generated by Django 5.0.3 on 2024-05-19 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_post_cat_alter_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]
