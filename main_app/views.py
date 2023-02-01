from django.shortcuts import render
# from django.views import View 
from django.views.generic.base import TemplateView
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.urls import reverse


from .models import MyPlant, Plant
# Create your views here.

# Home class 
class Home(TemplateView):
    template_name = "home.html"


# Plant info class 


class PlantInfo(TemplateView):
    template_name= "plant_info.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context ["plants"] = Plant.objects.filter(name__icontains=name)
            context["header"]= f"I am looking for {name}"
        else:    
            context ["plants"] = Plant.objects.all()
            context["header"] = "My plants"
        return context
# my plants 
class MyPlantList(TemplateView):
    template_name= "my_plant_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context ["myplants"] = MyPlant.objects.filter(name__icontains=name)
            context["header"]= f"I am looking for {name}"
        else:    
            context ["myplants"] = MyPlant.objects.all()
            context["header"] = "My plants"
        return context

class MyPlantCreate (CreateView):
    model= MyPlant
    fields =['name', 'img', 'description', 'watering_info']
    template_name="my_plant_create.html"
    success_url= "/myplants/"

class MyPlantDetail(DetailView):
    model = MyPlant
    template_name = "my_plant_detail.html"

class MyPlantUpdate (UpdateView):
    model = MyPlant
    fields = ['name', 'img', 'description', 'watering_info']
    template_name = "my_plant_update.html"
    # success_url= "/myplants/"
    def get_success_url(self):
        return reverse('my_plant_detail', kwargs={'pk': self.object.pk})

class MyPlantDelete(DeleteView):
    model = MyPlant
    template_name ="my_plant_delete_confirmation.html"
    success_url = "/myplants/"
# About 
class About(TemplateView):
    template_name= "about.html"

