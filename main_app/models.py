from django.db import models

# Create your models here.

class MyPlant(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    watering_info = models.TextField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Plant(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    propagate = models.TextField(max_length=500)
    toxic = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Water(models.Model):
    title = models.ForeignKey(MyPlant, on_delete=models.CASCADE, related_name="waters")
    complete = models.BooleanField(default=False)
    created = models.DateTimeField
    due = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return str(self.title)
