from django.urls import path
from .views import AddArticle,EditArticle,DeleteArticle,ArticlesListView,ArticleDetailView

urlpatterns = [
	path('',ArticlesListView.as_view(),name='home'),
	path('<int:pk>/',ArticleDetailView.as_view(),name='article'),
	path('new/', AddArticle.as_view(),name='addarticle'),
	path('<int:pk>/edit',EditArticle.as_view(),name='editarticle'),
	path('<int:pk>/delete/',DeleteArticle.as_view(),name='deletearticle'),
]