# Generated by Django 3.0.11 on 2021-04-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='to_publish',
            field=models.BooleanField(default=False, help_text='Demander la publication'),
        ),
    ]
