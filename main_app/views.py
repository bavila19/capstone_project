from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.urls import reverse
from django import forms
from django.forms import ModelForm
from .form import WaterForm
from django.views.decorators.http import require_POST
from .models import MyPlant, Plant,Water
from datetime import datetime



def WaterList(request, ):
    water_list = Water.objects.order_by('id')
    form = WaterForm()
    context = {'water_list': water_list, 'form': form}
    return render(request, 'water_list.html', context)

@require_POST 
def addWaterTodo(request):
    form = WaterForm(request.POST) 
    print(request.POST)
    if form.is_valid():
        plant = MyPlant.objects.get(pk=int(request.POST['title'][0]))
        datetime = request.POST.get("due")
        new_water_todo = Water(title = plant, due = datetime )
        new_water_todo.save()
    return redirect ('waterlist')
    
def CompleteWaterTodo(request, todo_id):
    todo = Water.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('waterlist')

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
    def get_success_url(self):
        return reverse('my_plant_detail', kwargs={'pk': self.object.pk})

class MyPlantDelete(DeleteView):
    model = MyPlant
    template_name ="my_plant_delete_confirmation.html"
    success_url = "/myplants/"

class About(TemplateView):
    template_name= "about.html"




