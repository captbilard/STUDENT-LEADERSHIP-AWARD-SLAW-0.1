from django import forms
from django.forms import TextInput, EmailInput, Select, NumberInput

# Third party import
from django_countries.widgets import CountrySelectWidget

from .models import Volunteers


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteers
        fields = ('__all__')
        widgets = {'Full_Name': TextInput(attrs={
            'class': "form-control form-control-sm",
            'placeholder': 'Enter your full name'
            }),
        'Email_Address': EmailInput(attrs={
                                    'class': "form-control form-control-sm",
                                    'placeholder': 'example@example.com'}),
        'Phone_Number': TextInput(attrs={
                                    'class': "form-control form-control-sm",
                                'placeholder': 'Enter your phone number'}),
        'Country': CountrySelectWidget(),
        'State': TextInput(attrs={'class': "form-control form-control-sm"}),
        'University': TextInput(attrs={
                                'class': "form-control form-control-sm"}),
        'Previous_volunteering_experience': Select(attrs={
                                                    'class': "form-control"}),
        'Are_you_currently_volunteering_for_an_NGO': Select(attrs={
                                                    'class': "form-control"})
        }
