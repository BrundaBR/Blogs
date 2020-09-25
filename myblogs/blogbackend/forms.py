from .models import BlogData
from django import forms

class Blogger(forms.ModelForm):

	class Meta:
		model=BlogData
		fields="__all__"