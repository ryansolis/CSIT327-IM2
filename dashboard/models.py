from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
	datereg = models.DateField(default = datetime.now())
	category = models.CharField(max_length = 100)
	name = models.CharField(max_length = 100)
	brand = models.CharField(max_length = 100)
	size = models.CharField(max_length = 50)
	color = models.CharField(max_length = 50)
	stocks = models.CharField(max_length = 5)
	price = models.CharField(max_length = 50)
	description = models.CharField(max_length = 10000)

	class Meta:
		db_table = "Product"