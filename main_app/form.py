from django import forms
from django.forms import Form
from .models import Water


class WaterForm(forms.Form):
    # template_name = "water_list.html"
    title= forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Water Task Title'}), label =  False)
    due= forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Due Date'}),label=False)

    class Meta :
        model = Water
        fields = ['title', 'due']
