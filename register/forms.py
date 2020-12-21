from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'email',)


class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password',)
