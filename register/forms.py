from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from register.models import UserProfile


class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email',)

	def clean_email(self):
		email = self.cleaned_data.get('email', False)  # if have email return it else return False
		if not email:
			raise forms.ValidationError('Email is required')
		return email


class LoginForm(AuthenticationForm):
	class Meta:
		model = User


class ProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ('user',)

