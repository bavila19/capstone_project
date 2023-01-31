from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('plantinfo/', views.PlantInfo.as_view(), name = "plant_info"),
    path('myplants/', views.MyPlantList.as_view(), name = "my_plant_list"),
    path('myplants/new', views.MyPlantCreate.as_view(), name = "my_plant_create"),


]