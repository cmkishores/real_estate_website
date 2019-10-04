from django.db import models

class Article(models.Model):

	# Choice fields for adverticement property type

	TYPE = [
			('FT','Flats'),
			('VL','Villas'),
			('LD','Land'),
			('CX','Shopping Complex'),

			]
	# Choice fields for the property condition
	CONDITION = [
			('NW','NEW'),
			('UD','Used'),
			('UC','Upcoming Project'),

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

	def __str__(self):
		return self.owner_name


	def get_absolute_url(self):
		return reverse('article',args=[str(self.id)])

	


# Create your models here.
