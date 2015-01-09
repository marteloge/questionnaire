from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from questionnaire.models import Person, Password
from django import forms
from questionnaire.forms import GenderForm
import sys

def index(request):
    model = Person
    template_name = 'questionnaire/index.html'

def view1(request):
    model = Person
    template_name = 'questionnaire/view1.html'
    return render(request, template_name)

def view2(request):
    model = Person
    template_name = 'questionnaire/view2.html'
    return render(request, template_name)

def add_gender(request):
    if request.method == 'POST':
        choice=request.POST['gender']
        # create a form instance and populate it with data from the request:
        form = GenderForm(request.POST)
        # check whether it's svalid:
        if form.is_valid():
            print >>sys.stderr, form.cleaned_data
            form.save()
            return HttpResponseRedirect('view1.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = GenderForm()
    return render(request, 'questionnaire/view1.html', {'form': form})
