from django.urls import path
from . import views

urlpatterns = [
    path('', views.NomineesView.as_view(), name="nominees"),
]