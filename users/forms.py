from .models import CustomUser 
from allauth.socialaccount.forms import SignupForm
#imports the custom user created in users.models
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(SignupForm):

	#This class creates a custom user creation form inheriting the built-in UserCreationForm and builts on top of that. 

	class Meta(UserCreationForm.Meta):

		model = CustomUser
		fields = ('username','email','category','mob_num')

class CustomUserChangeForm(UserChangeForm):

	# Custom user edit form 

	class Meta:

		model = CustomUser
		fields = ('username', 'email','category','mob_num')