from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationForm(UserCreationForm):

	#This class creates a custom user creation form inheriting the built-in UserCreationForm and builts on top of that. 

	class Meta(UserCreationForm.Meta):

		model = CustomUser
		fields = ('username','email','user_type')

class CustomUserChangeForm(UserChangeForm):

	# Custom user edit form 

	class Meta:

		model = CustomUser
		fields = ('username', 'email','user_type')