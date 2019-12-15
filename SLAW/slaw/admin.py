from django.contrib import admin

# Register your models here.
from .models import *


# class VoteInLine(admin.StackedInline):
#     model = Votes
#     extra = 1
    

class NomineesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {'fields': ['Award_Category']}),
        ('Nominees Details', {'fields':['Full_Name', 'Course_Of_Study', 'Level', 'Institution', 'Reason_for_nomination', 'CGPA'], 'classes':['collapse']})
    ]
    


admin.site.register(awardCategories)
admin.site.register(Nominees, NomineesAdmin)
admin.site.register(Votes)