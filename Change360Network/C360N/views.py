from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import VolunteerForm


def index(request):
    return render(request, "c360n/index.html")


def about_us(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your interest to volunteer with Change360Network, we will be in touch.')
            return redirect('about-us')
        messages.error(request, 'There was an issue with your form kindly check and fill again')
    else:
        form = VolunteerForm()
        return render(request, 'c360n/about-us.html', {'form': form})
