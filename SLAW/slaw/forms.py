from django import forms
from django.forms import TextInput, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Nominees, Votes

class NominateForm(forms.ModelForm):
    class Meta:
        model = Nominees
        fields = ['Award_Category', 'Full_Name', 'Course_Of_Study', 'Level', 'Institution', 'Reason_for_nomination', 'CGPA']
        widgets = {'Reason_for_nomination': Textarea(attrs={'cols':'40', 'row':'10'})}
    


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    school = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email','school','password1', 'password2']

    