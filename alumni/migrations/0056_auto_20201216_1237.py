# Generated by Django 3.0.8 on 2020-12-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0055_auto_20201204_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='instagram',
            field=models.URLField(blank=True, help_text='Adresse du compte instagram', null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='telegram',
            field=models.URLField(blank=True, help_text='Adresse public du compte telegram', null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='tiktok',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='vimeo',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
