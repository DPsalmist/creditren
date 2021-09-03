# Generated by Django 3.1.7 on 2021-03-18 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0008_auto_20210318_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='week',
            name='status',
        ),
        migrations.AddField(
            model_name='week',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='week',
            name='title',
            field=models.CharField(max_length=10, null='blank'),
            preserve_default='blank',
        ),
    ]