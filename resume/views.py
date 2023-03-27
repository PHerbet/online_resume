from django.shortcuts import render
from django.http import HttpResponse 
from .models import *

def index(resquest):
    return HttpResponse("test pour voir si ça marche ")

# Create your views here.