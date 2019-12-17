from django import forms
from django.forms import TextInput, Textarea
from .models import Nominees, Votes

class NominateForm(forms.ModelForm):
    class Meta:
        model = Nominees
        fields = ['Award_Category', 'Full_Name', 'Course_Of_Study', 'Level', 'Institution', 'Reason_for_nomination', 'CGPA']
        widgets = {'Reason_for_nomination': Textarea(attrs={'cols':'40', 'row':'10'})}
    
    # def save(self):
    #     nominee = super(NominateForm, self).save(commit=False)
    #     total_count = Nominees.objects.count()
    #     new_Nominee = Nominees.objects.get(pk=total_count)
    