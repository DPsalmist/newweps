from django.db import models
from django.contrib.auth.models import User

# Create your models here.
days = (
	('Monday','Monday'),
	('Tuesday','Tuesday'),
	('Wednesday','Wednesday'),
	('Thursday','Thursday'),
	('Friday','Friday'),
	('Saturday','Saturday'),
	)

categories = (
	('sports', 'sports'),
	('business', 'business'),
	('politics', 'politics'),
	('')
	)

class News(models.Model):
	title = models.CharField(max_length=60)
	body = models.TextField()
	date_created = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-date_created',)


class Club(models.Model):
 	name = models.CharField(max_length=60, unique=True)
 	instructor = models.CharField(blank=True, max_length=50, null=True)
 	meeting_day = models.CharField(max_length=10, choices=days, default='Saturday')
 	meeting_time = models.CharField(max_length=20, blank=True)
 	date_created = models.DateTimeField(auto_now=True)

 	def __str__(self):
 		return self.name

class Leadership(models.Model):
	name = models.CharField(max_length=30, blank=True)
	designation = models.CharField(max_length=50, blank=True)
	photo = models.ImageField(upload_to='leadership/', null=True, blank=True)
	date_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name