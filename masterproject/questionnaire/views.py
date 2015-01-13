from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from questionnaire.models import Person, Password
from django.contrib.sessions.models import Session
from django import forms
from questionnaire.forms import *
import sys

# print >>sys.stderr, choice

def index(request):
    model = Person
    template_name = 'questionnaire/index.html'
    return render(request, template_name, {'qnum': 1})

def add_handsize(request):
    person, created = Person.objects.get_or_create(pk=request.session.session_key)
    if request.method == 'POST':
        choice=request.POST['handsize']
        form=HandsizeForm(request.POST, instance=person)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('add_screensize')
    else:
        form=HandsizeForm(instance=person)
    return render(request, 'questionnaire/handsize.html', {'form':form, 'session':request.session['name']})

def add_screensize(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.method == 'POST':
        choice=request.POST['screensize']
        form=ScreensizeForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_handedness')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScreensizeForm(instance=person)
    return render(request, 'questionnaire/screensize.html', {'form': form, 'session': request.session['name']})

def add_handedness(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.method == 'POST':
        choice=request.POST['handedness']
        form=HandednessForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_finger')
    else:
        form = HandednessForm(instance=person)
    return render(request, 'questionnaire/handedness.html', {'form': form, 'session': request.session['name']})

def add_finger(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.method == 'POST':
        choice=request.POST['finger']
        form=FingerForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_reading')
    else:
        form = FingerForm(instance=person)
    return render(request, 'questionnaire/finger.html', {'form': form, 'session': request.session['name']})

def add_reading(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.method == 'POST':
        choice=request.POST['reading']
        form=ReadingForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_gender')
    else:
        form = ReadingForm(instance=person)
    return render(request, 'questionnaire/reading.html', {'form': form, 'session': request.session['name']})

def add_gender(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.method == 'POST':
        choice=request.POST['gender']
        form=GenderForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_age')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = GenderForm(instance=person)
    return render(request, 'questionnaire/gender.html', {'form': form, 'session': request.session['name']})

def add_age(request):
    model = Person
    template_name = 'questionnaire/age.html'
    return render(request, template_name, {'qnum': 1})

def add_nationality(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.method == 'POST':
        choice=request.POST['nationality']
        form=NationalityForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_usedALP')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NationalityForm(instance=person)
    return render(request, 'questionnaire/nationality.html', {'form': form, 'session': request.session['name']})

def add_usedALP(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.method == 'POST':
        choice=request.POST['used_ALP']
        form=UsedALPForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_useScreenlock')
    else:
        form = UsedALPForm(instance=person)
    return render(request, 'questionnaire/usedALP.html', {'form': form, 'session': request.session['name']})

def add_useScreenlock(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.method == 'POST':
        choice=request.POST['use_screenlock']
        form=UseScreenlockForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_screenlock')
    else:
        form = UseScreenlockForm(instance=person)
    return render(request, 'questionnaire/useScreenlock.html', {'form': form, 'session': request.session['name']})

def add_screenlock(request):
    person = Person.objects.get(pk=request.session.session_key)
    if request.method == 'POST':
        choice=request.POST['screenlock']
        form=ScreenlockForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_mobileOS')
    else:
        form = ScreenlockForm(instance=person)
    return render(request, 'questionnaire/screenlock.html', {'form': form, 'session': request.session['name']})

def add_mobileOS(request):
    model = Person
    template_name = 'questionnaire/mobileOS.html'
    return render(request, template_name, {'qnum': 1})

def add_experience(request):
    model = Person
    template_name = 'questionnaire/experience.html'
    return render(request, template_name, {'qnum': 1})

def finish(request):
    model = Person
    template_name = 'questionnaire/finish.html'
    return render(request, template_name, {'qnum': 1})

