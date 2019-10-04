from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.db.models.query_utils import query_utils

from django.contrib.auth models import Permission
from django.urls import reverse_lazy

from .models import Article
from django.conf import settings


class ArticlesListView(ListView):

	model = Article
	template_name = 'index.html'
	context_object_name = 'articlelist'
	login_url = 'login'


class ArticleDetailView(DetailView):

	model = Article
	template_name = 'article.html'

class AddArticle(CreateView):
	model = Article
	template_name = 'addarticle.html'
	fields = ['category','condition','owner_name','owner_address','description','location','photo']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class EditArticle(UpdateView):

	model = Article
	template_name = 'editarticle.html'
	fields = ['category','condition','owner_name','owner_address','description','location','photo']

class DeleteArticle(DeleteView):
	model = Article
	template_name = 'deletearticle.html'
	success_url = reverse_lazy('home')


