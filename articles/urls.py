from django.urls import path
from .views import AddArticle,EditArticle,DeleteArticle,ArticlesListView,ArticleDetailView

urlpatterns = [
	path('',ArticlesListView.as_view(),name='home'),
	path('property/<int:pk>/',ArticleDetailView.as_view(),name='article'),
	path('property/new/', AddArticle.as_view(),name='addarticle'),
	path('property/<int:pk>/edit',EditArticle.as_view(),name='editarticle'),
	path('property/<int:pk>/delete/',DeleteArticle.as_view(),name='deletearticle'),
]