from django.shortcuts import render, redirect

from .forms import VolunteerForm

# Create your views here.
def index(request):
    return render(request, "c360n/index.html")


def about_us(request):
    if request.method == 'POST':
        form  = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = VolunteerForm()
        return render(request, 'c360n/about-us.html', {'form':form})
