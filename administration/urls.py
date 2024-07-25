# administration/urls.py
from django.urls import path
from . import views

app_name = 'administration'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]
