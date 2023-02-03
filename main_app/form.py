from django import forms
from django.forms import Form
from .models import Water, MyPlant


class WaterForm(forms.Form):
    # template_name = "water_list.html"
    title= forms.ModelChoiceField(queryset = MyPlant.objects.all())
    due= forms.CharField(widget = forms.DateInput(attrs={'placeholder': 'Due Date', 'type': 'date'}, format=('%Y-%m-%d')),label=False)

    class Meta :
        model = Water
        fields = ['title_id', 'due']
