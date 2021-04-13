from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import NomineesListView, VoteView, UserViewSet, AwardCategoryViewSet

router = DefaultRouter()
router.register('nominees', NomineesListView, basename='nominees')
router.register('user', UserViewSet, basename='user')
router.register('award-category', AwardCategoryViewSet, basename='award-categories')

urlpatterns = [
    path('', include(router.urls)),
    path('vote/<int:nominee_id>/', VoteView.as_view())
]