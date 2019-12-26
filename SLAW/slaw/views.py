from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import logout
from .models import Nominees, Votes, awardCategories
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import NominateForm
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


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
@login_required
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
    

@login_required
def Nominate(request):
    if request.method == 'POST':
        nominate_form = NominateForm(request.POST)
        if nominate_form.is_valid():
            nominate_form.save()
        newNomineeId = Nominees.objects.count()
        try:
            newNominee = Nominees.objects.get(pk=newNomineeId+1)
        except (KeyError, Nominees.DoesNotExist):
            pass
        else:
            votesCreation = Votes(nominees=newNominee)
            votesCreation.save()
        return redirect('/')
    else:
        nominate_form = NominateForm()
        return render(request, 'slaw/nominate.html', {'form':nominate_form})

    
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = SignUpForm()
        return render(request, 'registration/register.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('index')