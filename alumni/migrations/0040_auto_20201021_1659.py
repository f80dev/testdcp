# Generated by Django 3.0.8 on 2020-10-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0039_auto_20201021_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='town',
            field=models.CharField(help_text='Adresse postale, ville', max_length=50, null=True),
        ),
    ]