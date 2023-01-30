from django.contrib import admin
from .models import MyPlant # import the Artist model from models.py
# Register your models here.

admin.site.register(MyPlant) # this line will add the model to the admin panel