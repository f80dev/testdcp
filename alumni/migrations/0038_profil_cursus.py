# Generated by Django 3.0.8 on 2020-10-21 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0037_auto_20201020_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='cursus',
            field=models.CharField(choices=[('S', 'Standard'), ('P', 'Professionnel')], default='S', max_length=1),
        ),
    ]