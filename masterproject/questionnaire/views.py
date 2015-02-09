from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from questionnaire.models import Person, Password
from django.contrib.sessions.models import Session
from django import forms
from questionnaire.forms import *
from django.forms.models import inlineformset_factory
from django.contrib import messages
import sys

# print >>sys.stderr, choice

def index(request):
    model = Person
    template_name = 'questionnaire/index.html'
    sys.stderr, request.mobile
    if request.mobile and not request.tablet:
        return render(request, 'questionnaire/index.html', {'mobile': True})
    else:
        return render(request, 'questionnaire/index.html', {'mobile': False})

def nomobile(request):
    template_name = 'questionnaire/nomobile.html'
    return render(request, template_name)

def rules(request):
    if request.mobile and not request.tablet:
        request.session.save()
        person, created = Person.objects.get_or_create(pk=request.session.session_key)
        if created:
            request.session.set_expiry(43200)
        return render(request, 'questionnaire/rules.html')
    return render(request, 'questionnaire/nomobile.html')
    
def training(request):
    person_id = request.session.session_key
    person = Person.objects.get(pk=person_id)

    if request.mobile and not request.tablet:
        if request.method == 'POST':
            password = Password(person_id=person_id, password_type='T')
            form = PatternForm(request.POST, instance=person)
            if form.is_valid():
                password.sequence = request.POST['sequence']
                password.save()
                if 'continue' in request.POST:
                    return HttpResponseRedirect('patterninformation')
                elif 'retry' in request.POST:
                    return HttpResponseRedirect('training')
        else:
            form = PatternForm(instance=person)
            return render(request, 'questionnaire/training.html', {'form': form})
    return render(request, 'questionnaire/nomobile.html')

def patterninformation(request):
    if request.mobile and not request.tablet:
        person = Person.objects.get(pk=request.session.session_key)
        return render(request, 'questionnaire/patterninformation.html')
    return render(request, 'questionnaire/nomobile.html')

def pattern1(request):
    person_id = request.session.session_key
    person = Person.objects.get(pk=person_id)

    if request.mobile and not request.tablet:
        if request.method == 'POST':
            password, created = Password.objects.get_or_create(person_id=person_id, password_type='1')
            form = PatternForm(request.POST, instance=person)
            if form.is_valid():
                password.sequence = request.POST['sequence']
                password.save()
                return HttpResponseRedirect('pattern2')
        else:
            form = PatternForm(instance=person)
            return render(request, 'questionnaire/pattern1.html', {'form': form})
    return render(request, 'questionnaire/nomobile.html')

def pattern2(request):
    person_id = request.session.session_key
    person = Person.objects.get(pk=person_id)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            password,created = Password.objects.get_or_create(person_id=person_id, password_type='2')
            form = PatternForm(request.POST, instance=person)
            if form.is_valid():
                password.sequence = request.POST['sequence']
                password.save()
                return HttpResponseRedirect('pattern3')
        else:
            form = PatternForm(instance=person)
            return render(request, 'questionnaire/pattern2.html', {'form': form})
    return render(request, 'questionnaire/nomobile.html')

def pattern3(request):
    person_id = request.session.session_key
    person = Person.objects.get(pk=person_id)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            password,created = Password.objects.get_or_create(person_id=person_id, password_type='3')
            form=PatternForm(request.POST, instance=person)
            if form.is_valid():
                password.sequence = request.POST['sequence']
                password.save()
                return HttpResponseRedirect('add_handsize')
        else:
            form = PatternForm(instance=person)
            return render(request, 'questionnaire/pattern3.html', {'form': form})
    return render(request, 'questionnaire/nomobile.html')

def add_handsize(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = HandsizeForm(request.POST, instance=person)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('add_screensize')
        else:
            form = HandsizeForm(instance=person)
            return render(request, 'questionnaire/handsize.html', {'form':form, 'qnum':1})
    return render(request, 'questionnaire/nomobile.html')

def add_screensize(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = ScreensizeForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('add_handedness')
        else:
            form = ScreensizeForm(instance=person)
            return render(request, 'questionnaire/screensize.html', {'form': form, 'qnum':2})
    return render(request, 'questionnaire/nomobile.html')

def add_handedness(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = HandednessForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('add_finger')
        else:
            form = HandednessForm(instance=person)
            return render(request, 'questionnaire/handedness.html', {'form': form, 'qnum':3})
    return render(request, 'questionnaire/nomobile.html')

def add_finger(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form=FingerForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('add_reading')
        else:
            form = FingerForm(instance=person)
            return render(request, 'questionnaire/finger.html', {'form': form, 'qnum':4, 'hand':person.handedness})
    return render(request, 'questionnaire/nomobile.html')

def add_reading(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = ReadingForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('add_gender')
        else:
            form = ReadingForm(instance=person)
            return render(request, 'questionnaire/reading.html', {'form': form, 'qnum':5})
    return render(request, 'questionnaire/nomobile.html')

def add_gender(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = GenderForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('add_age')
        else:
            form = GenderForm(instance=person)
            return render(request, 'questionnaire/gender.html', {'form': form, 'qnum':6})
    return render(request, 'questionnaire/nomobile.html')

def add_age(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = AgeForm(request.POST, instance=person)
            if form.is_valid():
                age = request.POST['age']
                if age.isdigit() and 16<=int(age)<= 99:
                    form.save()
                    return HttpResponseRedirect('add_nationality')
                else:
                    messages.error(request, age + ' is not a valid age. The age must be between 16 and 99.')
                    return HttpResponseRedirect('add_age')
            else:
                messages.error(request, 'This is not a valid input. Only numbers accepted!')
                return HttpResponseRedirect('add_age')
        else:
            form = AgeForm(instance=person)
            return render(request, 'questionnaire/age.html', {'form': form, 'qnum':7})
    return render(request, 'questionnaire/nomobile.html')

def add_nationality(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = NationalityForm(request.POST, instance=person)
            if form.is_valid():
                if (request.POST['nationality']=='0') or (request.POST['nationality']==0):
                    messages.error(request, 'You need to select your country before you can continue')
                    return HttpResponseRedirect('add_nationality')
                else:
                    form.save()
                    return HttpResponseRedirect('add_usedALP')
        else:
            form = NationalityForm(instance=person)
            return render(request, 'questionnaire/nationality.html', {'form': form, 'qnum':8})
    return render(request, 'questionnaire/nomobile.html')

def add_usedALP(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form=UsedALPForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('add_useScreenlock')
        else:
            form = UsedALPForm(instance=person)
            return render(request, 'questionnaire/usedALP.html', {'form': form, 'qnum':9})
    return render(request, 'questionnaire/nomobile.html')

def add_useScreenlock(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = UseScreenlockForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                if request.POST['use_screenlock']=='Y':
                    return HttpResponseRedirect('add_screenlock')
                elif request.POST['use_screenlock']=='N':
                    return HttpResponseRedirect('add_mobileOS')
        else:
            form = UseScreenlockForm(instance=person)
            return render(request, 'questionnaire/useScreenlock.html', {'form': form, 'qnum':10})
    return render(request, 'questionnaire/nomobile.html')

def add_screenlock(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = ScreenlockForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('add_mobileOS')
        else:
            form = ScreenlockForm(instance=person)
            return render(request, 'questionnaire/screenlock.html', {'form': form, 'qnum':11})
    return render(request, 'questionnaire/nomobile.html')

def add_mobileOS(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = OSForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('add_experience')
        else:
            form = OSForm(instance=person)
            return render(request, 'questionnaire/mobileOS.html', {'form': form, 'qnum':12})
    return render(request, 'questionnaire/nomobile.html')

def add_experience(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.mobile and not request.tablet:
        if request.method == 'POST':
            form = ExperienceForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('finish')
        else:
            form = ExperienceForm(instance=person)
            return render(request, 'questionnaire/experience.html', {'form': form, 'qnum':13})
    return render(request, 'questionnaire/nomobile.html')

def finish(request):
    if request.mobile and not request.tablet:
        model = Person
        template_name = 'questionnaire/finish.html'
        return render(request, template_name)
    return render(request, 'questionnaire/nomobile.html')
