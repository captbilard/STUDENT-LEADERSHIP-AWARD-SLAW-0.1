from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.date.today()
    html = "<html><body><p> the date is: %s </p></body></html>" % now
    return HttpResponse(html)