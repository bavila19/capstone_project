from django.contrib import admin
from .models import MyPlant, Water # import the Artist model from models.py
# Register your models here.

admin.site.register( MyPlant)
admin.site.register( Water)

# admin.site.register( Water) # this line will add the model to the admin panel
 # this line will add the model to the admin panel