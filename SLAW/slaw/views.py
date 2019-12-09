from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Nominees, Votes, awardCategories
import datetime

def index(request):
    categories = awardCategories.objects.all()
    return render(request, "slaw/index.html", {'categories':categories})



class NomineesView(generic.ListView):
    model = Nominees
    template_name = "slaw/nominees.html"
    context_object_name = 'nominee_list'

    
        
# def vote