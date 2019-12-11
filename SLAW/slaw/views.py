from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Nominees, Votes, awardCategories
import datetime


categories = awardCategories.objects.all()
categories_context = {'categories':categories}
def index(request):
    return render(request, "slaw/index.html", context=categories_context)



class NomineesView(generic.ListView):
    model = Nominees
    template_name = "slaw/nominees.html"
    context_object_name = 'nominee_list'

class VotingCategory(generic.ListView):
    model = awardCategories
    template_name = "slaw/voting-category.html"
    context_object_name = 'categories'
    # categories = awardCategories.objects.all()
    # return render(request, "slaw/voting-category.html", {'categories':categories})
        
# def voting(request, category_id):
#     category = get_object_or_404(awardCategories, pk=category_id)
#     return render(request, "slaw/nominee-list.html", {'category':category_id})

