from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Nominees, Votes
import datetime



class NomineesView(generic.ListView):
    template_name = "slaw/index.html"
    context_object_name = 'nominee_list'

    def get_queryset(self):
        # "Return all the nominees"
        return Nominees.objects.order_by('Award_Category')
        
        

# class NomineeDetailView(generic.DetailView):
