from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)
	text = models.TextField()
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title	

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	website = models.URLField(blank = True)
	picture = models.ImageField(upload_to = 'profile_images', blank=True)

	def __unicode__(self):
		return self.user.username