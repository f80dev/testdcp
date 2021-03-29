# Generated by Django 3.0.11 on 2021-03-29 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0069_auto_20210301_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='accept_tutor',
            field=models.BooleanField(default=False, help_text='Accept de tutoré un éleve'),
        ),
        migrations.AddField(
            model_name='profil',
            name='tutor',
            field=models.ForeignKey(help_text='Tuteur du profil', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='profil', to='alumni.Profil'),
        ),
    ]
