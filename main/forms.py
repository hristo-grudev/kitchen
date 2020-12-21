from django import forms

from .models import Recipes


class RecipesForm(forms.ModelForm):

	class Meta:
		model = Recipes
		fields = ('name',)
