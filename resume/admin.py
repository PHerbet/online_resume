
from django.contrib import admin
from .models import *
#import des modèles pour pouvoir les éditer avec la page admin
admin.site.register(Experience)
admin.site.register(Type_competence) 
admin.site.register(Competence) 
admin.site.register(Education) 
admin.site.register(Realisation) 
admin.site.register(Ressource)