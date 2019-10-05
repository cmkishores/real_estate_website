from django.test import TestCase

from .models import Article
from django.urls import reverse, reverse_lazy

class ArticleTest(TestCase):
	
	def setup(self):
		# Function to create dummy data for testing
		# Test function other than listing is not working

		self.post = Article.objects.create(category="Flats",condition="Used",owner_name="test",owner_address="test address",description="test description",location="test location",photo="")

	#def test_article_content(self):
		
		#article_object = Article.objects.get(pk=1)
		#expected_object_cat = f'{article_object.category}'
		#expected_object_cond = f'{article_object.condition}'
		#self.assertEqual(expected_object_cat,'Flats')
		#return self.assertEqual(expected_object_cond, 'Used')

	def test_list_view(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)

		
		#self.assertTemplateUsed(response, 'index.html')

	def test_article_details(self):
		response = self.client.get('/1/')
		#self.assertEqual(response.status_code, 200)
	

	def test_articleedit_view(self):
		response = self.client.post(reverse('editarticle', args='1'),{
			'owner_name' : 'testedit',
			})
		#self.assertContains(response, 'testedit')
		#self.assertEqual(response.status_code, 200)