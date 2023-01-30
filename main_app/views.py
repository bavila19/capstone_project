from django.shortcuts import render
# from django.views import View 
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# Create your views here.

# Home class 
class Home(TemplateView):
    template_name = "home.html"


# Plant info class 

class Plant:
    def __init__(self, name, image, description):
        self.name = name
        self.image = image
        self.description = description

# dummy data 
plants= [
    Plant("Monstera","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZ-WSf9QOWkz3ZO-JmqMcn9o-2FQyXNYd5lQ&usqp=CAU", "Monstera deliciosa, the Swiss cheese plant or split-leaf philodendron is a species of flowering plant native to tropical forests of southern Mexico, south to Panama. It has been introduced to many tropical areas, and has become a mildly invasive species in Hawaii, Seychelles, Ascension Island and the Society Islands"),
    Plant("Marble Queen Pothos", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_pfKnrrRTJIu8gAPan8_kX7qy7CkpScF7jz6XtbIH7oRe2sCDAlvS2icOPsuHIrlygMs&usqp=CAU", "Part of the aroid family, Araceae, it is a climbing vine, capable of growing to over 3m in height. It produces glossy bright green, oval-shaped leaves that are heavily spotted and streaked with cream-white colouring." )
      
]

class PlantInfo(TemplateView):
    template_name= "plant_info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["plants"] = plants
        return context
# My plant class 

# About 
class About(TemplateView):
    template_name= "about.html"
