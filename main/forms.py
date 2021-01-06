from django import forms

from .models import Recipes


class RecipesForm(forms.ModelForm):

	class Meta:
		model = Recipes
		fields = ('name',)


class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	from_email = forms.EmailField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)

	name.widget.attrs.update({'class': 'form-control', 'aria-describedby': "emailHelp", 'placeholder': "Enter name"})
	from_email.widget.attrs.update({'class': 'form-control', 'aria-describedby': "emailHelp", 'placeholder': "Enter email"})
	message.widget.attrs.update({'class': 'form-control', 'aria-describedby': "emailHelp", 'placeholder': "Enter name"})

	def clean(self):
		cleaned_data = super(ContactForm, self).clean()
		name = cleaned_data.get('name')
		from_email = cleaned_data.get('from_email')
		message = cleaned_data.get('message')
		if not name and not from_email and not message:
			raise forms.ValidationError('You have to write something!')
