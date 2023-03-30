from django.shortcuts import render
from django.http import HttpResponse 
from .models import *

def index(request):
    experiences = Experience.objects.all()
    type_competences = Type_competence.objects.all()
    competences = Competence.objects.all()
    educations = Education.objects.all()
    realisation = Realisation.objects.all()
    ressources = Ressource.objects.all()
    context = {
        'type_competences' : type_competences,
        'experiences' : experiences,
        'competences' : competences,
        'educations' : educations,
        'realisations' : realisation,
        'ressources' : ressources 
        }
    return render(request, 'resume/index.html', context)