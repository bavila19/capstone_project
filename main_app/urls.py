from django.urls import path
from . import views 
# from .views import redirect_view

urlpatterns = [
    #home & task list 
    # path('', views.Home, name="home"),
    # path('waterupdate/<int:pk>', views.WaterUpdate.as_view(), name="water_update"),
    # path('waterupdate/<int:pk>', views.WaterUpdate.as_view(), name="water_update"),
    path('', views.WaterList, name = "waterlist"),
    #about page
    path('about/', views.About.as_view(), name="about"),
    #plant info
    path('plantinfo/', views.PlantInfo.as_view(), name = "plant_info"),
    # My plant routes 
    path('myplants/', views.MyPlantList.as_view(), name = "my_plant_list"),
    path('myplants/new', views.MyPlantCreate.as_view(), name = "my_plant_create"),
    path('myplants/<int:pk>/', views.MyPlantDetail.as_view(), name = "my_plant_detail"),
    path('myplants/<int:pk>/update', views.MyPlantUpdate.as_view(), name = "my_plant_update"),
    path('myplants/<int:pk>/delete', views.MyPlantDelete.as_view(), name = "my_plant_delete"),

]