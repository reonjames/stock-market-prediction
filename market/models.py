from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user= models.ForeignKey(User,on_delete=models.CASCADE)
	name= models.CharField(max_length=30)
	email= models.CharField(max_length=30)
	password= models.CharField(max_length=50)
	question= models.CharField(max_length=40)
	answer= models.CharField(max_length=20)

	def __str__(self):
		return self.name
