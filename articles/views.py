from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.db.models.query_utils import Q
from django.shortcuts import get_list_or_404, get_object_or_404

from django.contrib.auth.models import Permission
from django.urls import reverse_lazy,reverse

from .models import Article,Comment
from django.conf import settings


class ArticlesListView(ListView):

	model = Article
	template_name = 'index.html'
	context_object_name = 'articlelist'
	

class ArticleDetailView(DetailView):

	model = Article
	template_name = 'articles.html'

class AddArticle(LoginRequiredMixin, CreateView):
	model = Article
	template_name = 'addarticle.html'
	fields = ['category','condition','owner_name','owner_address','description','price','location','photo']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class EditArticle(LoginRequiredMixin,UserPassesTestMixin, UpdateView):

	model = Article
	template_name = 'editarticle.html'
	fields = ['category','condition','owner_name','owner_address','description','price','location','photo']

	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user
	

class DeleteArticle(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = Article
	template_name = 'deletearticle.html'
	success_url = reverse_lazy('home')

	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user


class AddComment(LoginRequiredMixin,CreateView):
	model = Comment
	template_name='add_comment_to_post.html'
	fields = ['author','text']

	def form_valid(self, form):
		property_object = Article.objects.get(id=self.kwargs['pk'])
		form.instance.post = property_object
		return super().form_valid(form)