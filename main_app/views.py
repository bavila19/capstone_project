from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
# Create your views here.

# Home class 
class Home(View):
    def get(self, request):
        return HttpResponse ("Plant home")

# Plant info class 

# My plant class 