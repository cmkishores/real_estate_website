from django.contrib import admin
from .models import CustomUser # Imports custom user created in users.models
 
from .forms import CustomUserCreationForm, CustomUserChangeForm # Imports the two custom forms created in users.forms
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin) # Inherited from UserAdmin to customize the default admin panel display
	model = CustomUser
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	list_display = ['email','username','user_type',]
	fieldsets = UserAdmin.fieldsets + (
										 (None,
										 {'fields':('user_type',)}
										 ),
									   )
	add_fieldsets = (

		(None,{
			'classes':('wide'),
			'fields':('email','username','password1','password2','is_staff','is_active')
			}),
					)
	admin.site.register(CustomUser, CustomUserAdmin)