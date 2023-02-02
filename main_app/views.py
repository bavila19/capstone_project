from django.shortcuts import render, redirect
# from django.views import View 
from django.views.generic.base import TemplateView
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.urls import reverse
from django import forms
from django.forms import ModelForm

from .form import WaterForm


from .models import MyPlant, Plant,Water
# Create your views here.

# Home class 
# def WaterList(request):
#     queryset = Water.objects.order_by('title', 'due')
#     form = Water()
#     if request.method =='POST':
#         form=Water(request.Post)
#         if form.is_valid():
#             form.save()
#         return redirect ('/')
#     context = { 'waters': queryset,
#                 'form': forms}
#     return render(request, 'water_list.html', context)
def WaterList(request):
    water_list = Water.objects.order_by('id')
    form = WaterForm()
    context = {'water_list': water_list, 'form': form}
    return render(request, 'water_list.html', context)

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


