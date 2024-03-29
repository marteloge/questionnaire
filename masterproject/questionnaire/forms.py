from django import forms
from questionnaire.models import Person, Password

class TrainingForm(forms.ModelForm):
	class Meta:
		model = Password
		fields = ('sequence', 'password_type',)

class PatternForm(forms.ModelForm):
	class Meta:
		model = Password
		fields = ('sequence', 'time',)

class HandsizeForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('handsize',) 

class ScreensizeForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('screensize','actual_screenwidth', 'actual_screenheight',)

class HandednessForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('handedness',)

class Handedness2Form(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('handedness2',)

class FingerForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('finger',)

class ReadingForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('reading',)

class GenderForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('gender',)

class AgeForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('age',)

class NationalityForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('nationality',)

class UsedALPForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('used_ALP',)

class UseScreenlockForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('use_screenlock',)

class ScreenlockForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('screenlock',)

class OSForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('mobileOS',)

class ExperienceForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ('experience',)
