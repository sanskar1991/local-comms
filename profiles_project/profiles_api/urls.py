from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, basename='hello-viewset')

urlpatterns = [
    path('hello-world/', views.HelloAPI.as_view()),
    path('', include(router.urls))
]
