from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	template_name = 'signup.html'
	success_url = reverse_lazy('login')
	

# Create your views here.
