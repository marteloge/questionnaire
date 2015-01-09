from django.db import models

class Person(models.Model):
	handsize = models.CharField(max_length=2, default=0)
	screensize = models.CharField(max_length=2, default=0)
	finger = models.CharField(max_length=1, default=0)
	reading = models.CharField(max_length=2, default=0)
	gender = models.CharField(max_length=1, default=0)
	nationality = models.CharField(max_length=40, default=0)
	used_ALP = models.CharField(max_length=1, default=0)
	screen_lock = models.CharField(max_length=20, default=0)
	mobileOS = models.CharField(max_length=20, default=0)
	experience = models.CharField(max_length=1, default=0)

	def __unicode__(self):
		return "Person " + str(self.id)

class Password(models.Model): 
	person = models.ForeignKey(Person)
	password_type = models.CharField(max_length=1, default=0)
	sequence = models.CharField(max_length=20, default=0)

	def __unicode__(self):
		return "Password " + str(self.id)

		