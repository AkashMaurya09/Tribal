# Generated by Django 2.2.8 on 2020-01-08 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribal', '0005_auto_20200108_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produce',
            name='category',
        ),
        migrations.RemoveField(
            model_name='produce',
            name='image',
        ),
        migrations.RemoveField(
            model_name='produce',
            name='subcategory',
        ),
    ]