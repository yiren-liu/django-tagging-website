from django.urls import path

from . import views

urlpatterns = [
    path('', views.tagging, name='tagging'),
]
