from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

	# Two types of users sign up.  According to type, posting and other privilages are granted.
	TYPE = [
			('Seller','seller'),
			('Buyer','buyer'),

		]

	# CharField takes a maximum length of 50 characters and is limited to choices defined in the above dictionary
	category = models.CharField(max_length=50,choices=TYPE)
	mob_num = models.CharField(max_length=10)
