from django.db import models
from django.contrib.sessions.models import Session 

HANDSIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'XtraLarge'),
)
SCREENSICE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)
FINGER_CHOICES = (
	('F', 'Forefinger'),
    ('T', 'Thumb'),
)
READING_CHOICES = (
	('L', 'Left'),
    ('R', 'Right'),
    ('T', 'Top'),
)
GENDER_CHOICES = (
	('M', 'Male'),
    ('F', 'Female'),
)
HANDEDNESS_CHOICES = (
	('L', 'Left'),
    ('R', 'Right'),
)
YESNO_CHOICES = (
	('Y', 'Yes'),
    ('N', 'No'),
)
SCREENLOCK_CHOICES = (
	('pattern', 'pattern'),
    ('fingerprint', 'fingerprint'),
    ('PIN', 'PIN'),
    ('slide', 'slide'),
    ('other', 'other'),
)
MOBILEOS_CHOICES = (
	('android', 'Anroid'),
    ('ios', 'iOS'),
    ('windows', 'Windows'),
    ('blackberry', 'Blackberry'),
    ('no_android', 'No Android'),
    ('no_ios', 'No iOS'),
    ('no_windows', 'No Windows'),
    ('blackberry', 'No Blackberry'),
    ('unknown_android', 'Unknown Android'),
    ('unknown_ios', 'Unknown iOS'),
    ('unknown_windows', 'Unknown Windows'),
    ('unknown_blackberry', 'Unknown Blackberry'),
    ('other', 'Other'),
)

class Person(models.Model):
	handsize = models.CharField(max_length=2, default=0, choices=HANDSIZE_CHOICES)
	screensize = models.CharField(max_length=2, default=0, choices=SCREENSICE_CHOICES)
	finger = models.CharField(max_length=1, default=0, choices=FINGER_CHOICES)
	reading = models.CharField(max_length=2, default=0, choices=READING_CHOICES)
	gender = models.CharField(max_length=1, default=0, choices=GENDER_CHOICES)
	nationality = models.CharField(max_length=40, default=0)
	handedness = models.CharField(max_length=1, default=0, choices=HANDEDNESS_CHOICES)
	used_ALP = models.CharField(max_length=1, default=0, choices=YESNO_CHOICES)
	use_screenlock = models.CharField(max_length=1, default=0, choices=YESNO_CHOICES)
	screenlock = models.CharField(max_length=20, default=0, choices=SCREENLOCK_CHOICES)
	mobileOS = models.CharField(max_length=20, default=0, choices=MOBILEOS_CHOICES)
	experience = models.CharField(max_length=1, default=0, choices=YESNO_CHOICES)
	session_id = models.CharField(max_length=40, primary_key=True)
	age = models.IntegerField(max_length=2, default=0)
	actual_screenwidth = models.IntegerField(max_length=4, default=0)
	actual_screenheight = models.IntegerField(max_length=4, default=0)
	
	def __unicode__(self):
		return "Person " + str(self.session_id)

class Password(models.Model): 
	person = models.ForeignKey(Person)
	password_type = models.CharField(max_length=1, default=0)
	sequence = models.CharField(max_length=20, default=0)

	def __unicode__(self):
		return "Password " + str(self.id)

		