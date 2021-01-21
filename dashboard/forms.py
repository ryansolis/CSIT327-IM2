from django import forms
from .models import *

class ProductForm(forms.ModelForm):
	
	class Meta:
		model = Product
		fields = ('category', 'name', 'brand', 'size', 'color', 'stocks', 'price', 'description')