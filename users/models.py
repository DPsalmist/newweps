from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Staff(models.Model):
	first_name = models.CharField(max_length=50, blank=True)
	last_name = models.CharField(max_length=50, blank=True)
	username = models.ForeignKey(User, related_name='staff', on_delete=models.CASCADE, blank=True, null=True)
	gender = models.CharField(max_length=20, choices=(('male', 'male'), ('female','female')))
	designation = models.CharField(max_length=50, blank=True, default='staff')
	bio = models.CharField(max_length=200, blank=True)
	email = models.EmailField()
	dob = models.CharField(max_length=50, blank=True)
