# Generated by Django 3.0.8 on 2020-10-17 22:10

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0033_auto_20201018_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='auto_updates',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='Date de mise a jour', null=True),
        ),
    ]
