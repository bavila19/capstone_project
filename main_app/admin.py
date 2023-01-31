from django.contrib import admin
from .models import Plant # import the Artist model from models.py
# Register your models here.

admin.site.register( Plant) # this line will add the model to the admin panel