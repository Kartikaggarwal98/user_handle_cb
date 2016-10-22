from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user= models.OneToOneField(User)
	website= models.URLField(blank=True)
	score= models.IntegerField(blank=True)

	def __unicode__(self):
		return self.user.username
		