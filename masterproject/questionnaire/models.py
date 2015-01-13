from django.db import models
from django.contrib.sessions.models import Session 

class Person(models.Model):
	handsize = models.CharField(max_length=2, default=0)
	screensize = models.CharField(max_length=2, default=0)
	finger = models.CharField(max_length=1, default=0)
	reading = models.CharField(max_length=2, default=0)
	gender = models.CharField(max_length=1, default=0)
	nationality = models.CharField(max_length=40, default=0)
	handedness = models.CharField(max_length=1, default=0)
	used_ALP = models.CharField(max_length=1, default=0)
	use_screenlock = models.CharField(max_length=1, default=0)
	screenlock = models.CharField(max_length=20, default=0)
	mobileOS = models.CharField(max_length=20, default=0)
	experience = models.CharField(max_length=1, default=0)
	session_id = models.CharField(max_length=40, primary_key=True)
	age = models.IntegerField(max_length=2, default=0)

	def __unicode__(self):
		return "Person " + str(self.session_id)

class Password(models.Model): 
	person = models.ForeignKey(Person)
	password_type = models.CharField(max_length=1, default=0)
	sequence = models.CharField(max_length=20, default=0)

	def __unicode__(self):
		return "Password " + str(self.id)

		