from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="blog-hhomepage"),
    # path('about_us/', views.about_us, name="about-us"),
]
