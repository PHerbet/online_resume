from django.db import models

#création des différents modèles :

class Experience(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    period = models.CharField(max_length=25)
    mission = models.TextField()
    icon_company = models.ImageField(
        upload_to="icon_company", 
        blank=True, 
        null=True,
        )
    
    def __str__(self):
        return self.position


class Type_competence(models.Model):
    name_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_type


class Competence(models.Model):
    name_competence = models.CharField(max_length=50)
    icon_competence = models.ImageField(
        upload_to="icon_competence", 
        blank=True, 
        null=True,
        )
    type_competence = models.ForeignKey(
        'Type_competence',
        models.SET_NULL,
        null=True,
        )

    def __str__(self):
        return self.name_competence


class Education(models.Model):
    title = models.CharField(max_length=25)
    obtention_year = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Realisation(models.Model):
    name_realisation = models.CharField(max_length=25)
    description = models.TextField()
    git_link = models.SlugField(max_length=200)
    icon_realisation = models.ImageField(
        upload_to="icon_realisation", 
        blank=True, 
        null=True,
        )
    def __str__(self):
        return self.name_realisation


class Ressource(models.Model):
    name_ressource = models.CharField(max_length=20)
    url_ressource = models.SlugField(max_length=200)
    icon_ressource = models.ImageField(
        upload_to="icon_ressource", 
        blank=True, 
        null=True,
        )
    def __str__(self):
        return self.name_ressource