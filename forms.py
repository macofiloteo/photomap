from django import forms
from .models import ImageSpot

class ImageForm(forms.ModelForm):
        geodata = forms.CharField()
        layer_name = forms.CharField()

        class Meta:
        	model = ImageSpot
        	fields = ["image"]