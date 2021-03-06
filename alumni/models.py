import datetime
from dataclasses import Field

import django
from django.contrib.auth.models import AbstractUser, User
from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models

# Create your models here.
#Mise a jour du model : python manage.py makemigrations
from django.db.models import Model, CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry

from OpenAlumni.Tools import now
from OpenAlumni.settings import DOMAIN_APPLI



class Profil(models.Model):
    """
    Le profil stocke l'ensemble des informations sur les anciens étudiants, issue du cursus standard ou pro
    """
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=40, null=False, default='',help_text="Prénom du profil")
    lastname=models.CharField(max_length=70, null=False, default='',help_text="Nom du profil")
    birthdate=models.DateField(null=True,help_text="Date de naissance")
    mobile=models.CharField(blank=True,max_length=20,null=True,default="06",help_text="Numéro de mobile")
    nationality=models.CharField(blank=True,max_length=30,null=False,default="Française")
    department=models.CharField(blank=True,max_length=60,null=True,default="",help_text="Cursus suivi pendant les études")
    job=models.CharField(max_length=60,null=True,default="",blank=True,help_text="Profession actuelle")
    degree_year=models.IntegerField(null=True,help_text="Année de sortie de l'école")

    linkedin = models.URLField(blank=True, null=True,help_text="Adresse de la page public linkedin du profil")
    email=models.EmailField(null=False,unique=True,help_text="email du profil")
    instagram=models.URLField(blank=True, null=True,help_text="Adresse du compte instagram")
    telegram=models.URLField(blank=True, null=True,help_text="Adresse public du compte telegram")
    facebook=models.URLField(blank=True, null=True,help_text="Adresse de la page facebook du profil")
    twitter=models.URLField(blank=True, null=True,help_text="Adresse de la page twitter du profil")
    tiktok=models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    vimeo=models.URLField(blank=True, null=True)

    acceptSponsor = models.BooleanField(null=False, default=False)
    sponsorBy = models.ForeignKey('Profil', null=True,on_delete=CASCADE)

    photo=models.TextField(blank=True,help_text="Photo du profil au format Base64")
    gender=models.CharField(max_length=1,blank=False,default="M",choices=(('M','Male'),('F','Female'),('N','Non précisé')))
    cursus=models.CharField(max_length=1,blank=False,default="S",choices=(('S','Standard'),('P','Professionnel')),help_text="Type de formation")
    address=models.CharField(null=True,blank=True,max_length=200,help_text="Adresse postale au format numéro / rue / batiment")
    town = models.CharField(null=True,blank=True,max_length=50, help_text="Ville de l'adresse postale")
    cp=models.CharField(null=True,blank=True,max_length=5,help_text="code postal de l'adresse postale")
    website=models.URLField(null=True)
    dtLastUpdate=models.DateTimeField(null=False,auto_now=True,help_text="Date de la dernière modification du profil")
    dtLastSearch=models.DateTimeField(null=False,auto_now=True,help_text="Date de la dernière recherche d'expérience pour le profil")
    dtLastNotif=models.DateTimeField(null=False,auto_now=True,help_text="Date de la dernière notification envoyé")
    obsolescenceScore=models.IntegerField(default=0,help_text="Indique le degré d'obsolescence probable")
    biography=models.TextField(null=True,max_length=2000,help_text="Biographie du profil")
    links = JSONField(null=True, help_text="Liens vers des références externes au profil")
    auto_updates=models.CharField(max_length=300,null=False, default="0,0,0,0,0,0",help_text="Date de mise a jour")
    advices=JSONField(null=True,help_text="Liste de conseils alimenter par l'outil pour augmenter le rayonnement d'une personne")

    class Meta(object):
        ordering=["lastname"]

    def delay_update(self,_type,update=False):
        """
        :return: delay de mise a jour en heure
        """
        lastUpdates = self.auto_updates.replace("[", "").replace("]", "").split(",")
        rc=(datetime.datetime.now().timestamp() - float(lastUpdates[_type]))/3600
        if update:
            lastUpdates[_type]=str(datetime.datetime.now().timestamp())
            self.auto_updates=",".join(lastUpdates)

        return rc

    def delay_lastsearch(self):
        """
        :return: delay de mise a jour en heure
        """
        rc=(datetime.datetime.now().timestamp() - self.dtLastSearch.timestamp())/3600
        return rc


    def add_link(self,url,title,description=""):
        if self.links is None:self.links=[]
        obj={"url":url,"text":title,"update":now(),"desc":description}
        for l in self.links:
            if l["url"]==url:
                self.links.remove(l)
                break

        self.links.append(obj)
        return self.links


    @property
    def public_url(self):
        return DOMAIN_APPLI+"/?id="+str(self.id)

    @property
    def promo(self):
        return str(self.degree_year)

    @property
    def fullname(self):
        return '%s %s' % (self.firstname, self.lastname)

    @property
    def str_links(self):
        if self.links is None:return ""
        s=""
        for l in self.links:
            s=s+l.url+";"
        return s

    def __str__(self):
        return "{'id':"+str(self.id)+",'email':'"+self.email+"','fullname':'"+self.fullname+"'}"

    @property
    def name_field_indexing(self):
        return {"name":self.lastname+" "+self.firstname}




class Article(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Profil, null=False, on_delete=models.CASCADE, related_name="Articles",help_text="Auteur de l'article")
    validate=models.BooleanField(default=False,null=False,help_text="Une fois à vrai l'article est visible de tous")
    html=models.TextField(max_length=5000, blank=True,default="",help_text="Contenu de l'article")
    dtPublish = models.DateField(null=True, help_text="Date de publication de l'article")
    dtCreate = models.DateField(auto_now=True, null=False, help_text="Date de création de l'article")
    tags=models.CharField(max_length=100,default="")
    to_publish=models.BooleanField(default=False,null=False,help_text="Demander la publication")

    class Meta:
        ordering = ["dtCreate"]


#Gestion du modele UserExtra______________________________________________________________________________________
class ExtraUser(models.Model):
    """
    Classe supplémentaire pour gérer les permissions par utilisateur
    voir https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="extrauser")
    perm = models.TextField(max_length=500, blank=True,default="")
    profil_name=models.CharField(max_length=50,default="",blank=True)
    black_list=models.TextField(help_text="Contient l'ensemble des emails ne pouvant contacter la personne",null=False,default="")
    profil=models.OneToOneField(Profil,on_delete=models.CASCADE,null=True)

    level=models.IntegerField(default=0,help_text="Niveau de l'utilisateur")
    ask=ArrayField(base_field=models.IntegerField(null=False,default=0),null=True)
    friends=ArrayField(base_field=models.IntegerField(null=False,default=0),null=True)


class Work(models.Model):
    """
    Réalisation / projets des profils
    Cet objet permet de faire le lien entre les oeuvres et les profils
    Il peut être alimenté en automatique (par scrapping des sources) ou en manuel par le profil
    """
    id = models.AutoField(primary_key=True,help_text="Clé primaire interne des projets")
    profil = models.ForeignKey('Profil', null=False, on_delete=models.CASCADE,related_name="works",help_text="Profil concerné par le projet")
    pow = models.ForeignKey('PieceOfWork', null=False, on_delete=models.CASCADE, related_name="works",help_text="oeuvre concerné par le projet")
    status=models.CharField(max_length=200,default="")
    state=models.CharField(max_length=1,default="A",help_text="etat du travail entre A=automatiquement creer,E=editer par le profil, D=supprimé par le profil")

    #creator passera à user si l'utilisateur modifie l'enregistrement
    creator=models.CharField(max_length=5,default="auto",help_text="Désigne qui est le dernier auteur de l'enregistrement dans la base de données")
    public=models.BooleanField(default=True,help_text="Indique si le projet est publique (visible de ceux qui ont les droits) ou privé")

    job=models.CharField(max_length=200,default="",help_text="Rôle dans le projet")
    duration=models.IntegerField(default=0,null=False,help_text="Durée du projet en heure")
    comment=models.TextField(max_length=400,null=False,default="",blank=True,help_text="Commentaire sur la façon dont s'est passé le projet")
    earning=models.IntegerField(default=None,null=True,help_text="Revenu percu brut pour la durée annoncée")
    source=models.CharField(max_length=100,null=False,default="",help_text="source ayant permis d'identifier le projet : imdb, unifrance, bellefaye, manuel")
    validate=models.BooleanField(default=False,help_text="Indique si l'expérience est validé ou pas")

    @property
    def title(self):
        return self.pow.title


    @property
    def year(self):
        return self.pow.year

    @property
    def nature(self):
        return self.pow.nature


    @property
    def lastname(self):
        return self.profil.lastname


    def __str__(self):
        d:dict=dict({
            "name":self.profil.firstname+" "+self.profil.lastname,
            "job":self.job,
            "dtStart":str(self.dtStart),
            "comment":self.comment,
        })
        if self.pow is not None:d["pow"]={"title":self.pow.title}

        return str(d)




class PieceOfWork(models.Model):
    """
    Description des oeuvres

    """
    id = models.AutoField(primary_key=True)
    budget=models.IntegerField(default=0,help_text="Coût total de réalisation de l'oeuvre")
    visual = models.TextField(blank=True,help_text="Visuel de l'oeuvre")
    dtStart=models.DateField(auto_now=True,null=False,help_text="Date de début de la réalisation de l'oeuvre")
    dtEnd=models.DateField(auto_now=True,null=False,help_text="Date de fin de la réalisation de l'oeuvre")
    title=models.CharField(null=False,max_length=300,unique=True,default="sans titre",help_text="Titre de l'oeuvre, même temporaire")
    year=models.CharField(null=True,max_length=4,help_text="Année de sortie")
    nature=models.CharField(null=False,default='MOVIE',max_length=20,help_text="Classification de l'oeuvre")
    dtCreate = models.DateField(auto_now_add=True,help_text="Date de création de l'oeuvre")

    #Structure : "url" du document, "text" du lien
    links=JSONField(null=True,help_text="Liens vers des références externes à l'oeuvre")

    owner=models.CharField(max_length=150,default="public",help_text="Auteur de l'oeuvre")
    description=models.TextField(null=False,default="",max_length=3000,help_text="Description/Resumer de l'oeuvre")
    # Structure : "url" du document, "type" de document (str), "title" du document
    files=JSONField(null=True,help_text="Liens vers des documents attaché")
    category=models.TextField(null=True,max_length=200,help_text="Liste des categories auxquelles appartient le film")
    lang=models.CharField(max_length=50,null=True,help_text="Langue originale de l'oeuvre")


    def __str__(self):
        return self.title

    def add_link(self, url, title, description=""):
        if self.links is None: self.links = []
        obj = {"url": url, "text": title, "update": now(), "desc": description}
        for l in self.links:
            if l["url"] == url:
                self.links.remove(l)
                break

        self.links.append(obj)
        return self.links


@receiver(post_save,sender=Work)
def update_pow(sender, **kwargs):
    instance = kwargs['instance']
    registry.update(instance.profil)


class Movie(PieceOfWork):
    duration = models.DurationField(null=True,help_text="Durée du film")



# class School(models.Model):
#     name = models.TextField(max_length=100)


# class Degree(models.Model):
#     profil = models.ForeignKey('Profil',null=False,on_delete=models.CASCADE)
#     school = models.ForeignKey('School',null=False,on_delete=models.CASCADE)
#     dtCreate = models.DateField(auto_now_add=True)


