from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import NomineesListView, VoteView, UserViewSet

router = DefaultRouter()
router.register('nominees', NomineesListView, basename='nominees')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('vote/<int:nominee_id>/', VoteView.as_view())
]