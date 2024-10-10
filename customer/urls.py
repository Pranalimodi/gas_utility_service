# customer/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('submit/', views.request_service, name='submit_service'),
    path('requests/', views.request_list, name='request_list'),
]
