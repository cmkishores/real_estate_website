from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime

class Article(models.Model):

	# Choice fields for adverticement property type

	TYPE = [
			('Flats','Flats'),
			('Villas','Villas'),
			('Land','Land'),
			('Shopping Complex','Shopping Complexes'),

			]
	# Choice fields for the property condition
	CONDITION = [
			('New','NEW'),
			('Used','Used'),
			('Upcoming project','Upcoming Project'),

		]
	class Meta:
		verbose_name = 'Article'


	category = models.CharField(max_length=30,choices=TYPE)
	condition = models.CharField(max_length=30,choices=CONDITION)
	owner_name = models.CharField(max_length=40)
	owner_address = models.TextField()
	description = models.TextField()
	location = models.TextField()
	photo = models.ImageField(upload_to='images/',blank=True)
	owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	price = models.PositiveIntegerField(default=10000)
	created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

	def __str__(self):
		return self.owner_name


	def get_absolute_url(self):
		return reverse('article',args=[str(self.id)])

	

#Comment model for posts 
class Comment(models.Model):
    post = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)