# Generated by Django 3.0.8 on 2020-10-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0047_auto_20201023_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='source',
            field=models.URLField(null=True),
        ),
    ]