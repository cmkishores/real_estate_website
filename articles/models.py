from django.db import models

class Article(models.Model):

	# Choice fields for adverticement property type

	TYPE = [
			('FT','Flats'),
			('VL','Villas'),
			('LD','Land'),
			('CX','Shopping Complex'),

			]

	CONDITION = [
			('NW','NEW'),
			('UD','Used'),
			('UC','Upcoming Project'),

		]
	class Meta:
		verbose_name = 'Article'


	type = models.CharField(max_length=30,choices=TYPE)
	condition = models.CharField(max_length=30,choices=CONDITION)
	owner_name = models.CharField(max_length=40)


# Create your models here.
