from django import forms
from questionnaire.models import Person

class GenderForm(forms.ModelForm):
    CHOICES=[('M','M'), ('F','F')]
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Person
        fields = ('gender',)