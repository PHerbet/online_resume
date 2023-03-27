from django.db import models

#création des différents modèles :

class Experience(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    period = models.CharField(max_length=25)
    mission = models.TextField()
    icon_company = models.CharField(max_length=100)

class Type_competence(models.Model):
    name_type = models.CharField(max_length=50)

class Competence(models.Model):
    name_competence = models.CharField(max_length=50)
    image_competence = models.CharField(max_length=100)
    type_competence = models.ForeignKey(
        'Type_competence',
        models.SET_NULL,
        null=True,
        )

class Education(models.Model):
    title = models.CharField(max_length=25)
    obtention_year = models.CharField(max_length=10)

class Realisation(models.Model):
    name_realisation = models.CharField(max_length=25)
    description = models.TextField()
    git_link = models.CharField(max_length=200)
    image_realisation = models.CharField(max_length=100)

class Ressource(models.Model):
    name_resssource = models.CharField(max_length=20)
    url_ressource = models.CharField(max_length=100)
    icon_ressource = models.CharField(max_length=100)
