# Generated by Django 3.0.11 on 2021-01-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0057_auto_20201217_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='job',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
    ]