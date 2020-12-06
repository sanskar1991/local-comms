from django.urls import path

from . import views

urlpatterns = [
    path('hello-world/', views.HelloAPI.as_view()),
]
