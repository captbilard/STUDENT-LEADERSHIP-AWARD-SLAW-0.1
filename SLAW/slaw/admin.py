from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(awardCategories)
admin.site.register(Nominees)
admin.site.register(Votes)