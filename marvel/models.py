from django.db import models




class Heroe(models.Model):
	nombre = models.CharField(max_length=140)
	desc = models.TextField()
	img = models.CharField(max_length=500)

	def __str__(self):
		return self.nombre