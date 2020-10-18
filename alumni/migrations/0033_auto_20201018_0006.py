# Generated by Django 3.0.8 on 2020-10-17 22:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0032_profil_obsolescencescore'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='links',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='Liens vers des références externes au profil', null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='address',
            field=models.TextField(help_text='Adresse postale, rue', null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='cp',
            field=models.IntegerField(help_text='Adresse postale, code postal', null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='town',
            field=models.TextField(help_text='Adresse postale, ville', null=True),
        ),
    ]
