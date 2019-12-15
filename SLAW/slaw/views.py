from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Nominees, Votes, awardCategories
from django.urls import reverse
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
        
def votingList(request, category_id):
    category = get_object_or_404(awardCategories, pk=category_id)
    return render(request, "slaw/voting-list.html", {'category':category})

def vote(request, nominee_id):
    nominee = get_object_or_404(Nominees, pk=nominee_id)
    # print(nominee_id)
    # selected_nominee = nominee.votes_set.get(pk=nominee_id -1)
    # print(selected_nominee)
    # return HttpResponseRedirect(reverse('index'))
    try:
        selected_nominee = nominee.votes_set.get(pk=nominee_id - 1)
    except (KeyError, Votes.DoesNotExist):
        return render(request, 'slaw/voting-list.html', {'error_message':"You didn't select a nominee"})
    else:
        print(selected_nominee)
        selected_nominee.number_of_votes += 1
        selected_nominee.save()
        return HttpResponseRedirect(reverse('index'))
    


 

