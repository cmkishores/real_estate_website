from django.test import TestCase

from .models import Article
from django.urls import reverse, reverse_lazy

class ArticleTest(TestCase):
	def setup(self):
		# Function to create dummy data for testing

		self.post = Article.objects.create(category="Flats",condition="Used",owner_name="test",owner_address="test address",description="test description",location="test location",owner="cmk")

# Create your tests here.
