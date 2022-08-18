from django.db import models

# Create your models here.

class Product(models.Model):
	
	maxsulot_nomi=models.CharField(max_length=150)
	tarkibi=models.TextField()
	narxi=models.CharField(max_length=14)
	img=models.ImageField(upload_to='img/')

	def __str__(self):
		return self.maxsulot_nomi

