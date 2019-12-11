from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nominees/', views.NomineesView.as_view(), name="nominees"),
    path('vote/', views.VotingCategory.as_view(), name="voting-category"),

    
]