from django.urls import path

from . import views

urlpatterns = [
    path('', views.tagging, name='tagging'),
    path('reset_test_database/', views.reset_test_database, name='reset_test_database'),
    path('download_as_csv/', views.download_as_csv, name='download_as_csv'),
]
