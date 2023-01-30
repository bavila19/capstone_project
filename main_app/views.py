from django.shortcuts import render
# from django.views import View 
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# Create your views here.

# Home class 
class Home(TemplateView):
    template_name = "home.html"


# Plant info class 

# My plant class 

# About 
class About(TemplateView):
    template_name= "about.html"