from django.contrib import admin

from .models import Nominees, AwardCategories
# Register your models here.
admin.site.register(Nominees)
admin.site.register(AwardCategories)