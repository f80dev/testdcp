# Generated by Django 3.0.11 on 2021-01-14 10:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0061_extrauser_profil_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieceofwork',
            name='lang',
            field=models.CharField(help_text="Langue originale de l'oeuvre", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pieceofwork',
            name='owner',
            field=models.CharField(default='public', help_text="Auteur de l'oeuvre", max_length=150),
        ),
        migrations.AlterField(
            model_name='profil',
            name='address',
            field=models.CharField(blank=True, help_text='Adresse postale au format numéro / rue / batiment', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='advices',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text="Liste de conseils alimenter par l'outil pour augmenter le rayonnement d'une personne", null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='biography',
            field=models.TextField(help_text='Biographie du profil', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='birthdate',
            field=models.DateField(help_text='Date de naissance', null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='cp',
            field=models.CharField(blank=True, help_text="code postal de l'adresse postale", max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='cursus',
            field=models.CharField(choices=[('S', 'Standard'), ('P', 'Professionnel')], default='S', help_text='Type de formation', max_length=1),
        ),
        migrations.AlterField(
            model_name='profil',
            name='degree_year',
            field=models.IntegerField(help_text="Année de sortie de l'école", null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='department',
            field=models.CharField(blank=True, default='', help_text='Cursus suivi pendant les études', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='email',
            field=models.EmailField(help_text='email du profil', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='facebook',
            field=models.URLField(blank=True, help_text='Adresse de la page facebook du profil', null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='firstname',
            field=models.CharField(default='', help_text='Prénom du profil', max_length=40),
        ),
        migrations.AlterField(
            model_name='profil',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Non précisé')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='profil',
            name='job',
            field=models.CharField(blank=True, default='', help_text='Profession actuelle', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='lastname',
            field=models.CharField(default='', help_text='Nom du profil', max_length=70),
        ),
        migrations.AlterField(
            model_name='profil',
            name='linkedin',
            field=models.URLField(blank=True, help_text='Adresse de la page public linkedin du profil', null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='mobile',
            field=models.CharField(blank=True, default='06', help_text='Numéro de mobile', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='photo',
            field=models.TextField(blank=True, help_text='Photo du profil au format Base64'),
        ),
        migrations.AlterField(
            model_name='profil',
            name='town',
            field=models.CharField(blank=True, help_text="Ville de l'adresse postale", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='twitter',
            field=models.URLField(blank=True, help_text='Adresse de la page twitter du profil', null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='comment',
            field=models.TextField(blank=True, default='', help_text="Commentaire sur la façon dont s'est passé le projet", max_length=400),
        ),
        migrations.AlterField(
            model_name='work',
            name='creator',
            field=models.CharField(default='auto', help_text="Désigne qui est le dernier auteur de l'enregistrement dans la base de données", max_length=5),
        ),
        migrations.AlterField(
            model_name='work',
            name='dtEnd',
            field=models.DateField(help_text='Date de fin du projet', null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='dtStart',
            field=models.DateField(help_text='Date de début du projet', null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='duration',
            field=models.IntegerField(default=0, help_text='Durée du projet en heure'),
        ),
        migrations.AlterField(
            model_name='work',
            name='id',
            field=models.AutoField(help_text='Clé primaire interne des projets', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='work',
            name='job',
            field=models.CharField(default='', help_text='Rôle dans le projet', max_length=200),
        ),
        migrations.AlterField(
            model_name='work',
            name='pow',
            field=models.ForeignKey(help_text='oeuvre concerné par le projet', on_delete=django.db.models.deletion.CASCADE, related_name='works', to='alumni.PieceOfWork'),
        ),
        migrations.AlterField(
            model_name='work',
            name='profil',
            field=models.ForeignKey(help_text='Profil concerné par le projet', on_delete=django.db.models.deletion.CASCADE, related_name='works', to='alumni.Profil'),
        ),
        migrations.AlterField(
            model_name='work',
            name='public',
            field=models.BooleanField(default=True, help_text='Indique si le projet est publique (visible de ceux qui ont les droits) ou privé'),
        ),
        migrations.AlterField(
            model_name='work',
            name='source',
            field=models.CharField(default='', help_text="source ayant permis d'identifier le projet : imdb, unifrance, bellefaye", max_length=100),
        ),
    ]