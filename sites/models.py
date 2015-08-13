from django.db import models

# Create your models here.


class site(models.Model):
	nome = models.CharField(max_length=70, blank=False)
	host_ftp = models.CharField(max_length=50, blank=False)
	pass_ftp = models.CharField(max_length=50, blank=False)
	user_ftp = models.CharField(max_length=50, blank=False)
	name_db = models.CharField(max_length=50)
	host_db = models.CharField(max_length=50)
	user_db = models.CharField(max_length=50)
	pass_db = models.CharField(max_length=50)
	prefix_db = models.CharField(max_length=30, blank=True)
	
	def __str__(self):
		return self.nome
	

