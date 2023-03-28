from django.shortcuts import render
from django.http import HttpResponse 
from .models import *

def index(request):
    experiences = Experience.objects.all()
    context = {'experiences' : experiences}
    return render(request, 'resume/index.html', context)


