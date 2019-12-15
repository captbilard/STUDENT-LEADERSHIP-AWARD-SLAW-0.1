from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nominees/', views.NomineesView.as_view(), name="nominees"),
    path('vote-category/', views.VotingCategory.as_view(), name="voting-category"),
    path('vote-category/<int:category_id>/', views.votingList, name="voting-list"),
    path('<int:nominee_id>/vote/', views.vote, name="vote")

    
]