# Generated by Django 3.0.4 on 2020-03-09 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20200309_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_vid',
            field=models.CharField(default='', max_length=100),
        ),
    ]
