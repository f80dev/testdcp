# Generated by Django 3.0.8 on 2020-10-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0041_auto_20201022_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='cp',
            field=models.CharField(help_text='Adresse postale, code postal', max_length=5, null=True),
        ),
    ]