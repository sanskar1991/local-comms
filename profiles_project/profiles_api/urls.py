from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
# router.register('hello-viewset', views.HelloViewSets, basename='hello-viewset')
router.register('profile', views.UserProfileViewSets)

urlpatterns = [
    path('', include(router.urls))
]
