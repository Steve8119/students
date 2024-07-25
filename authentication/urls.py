# authentication/urls.py

from django.urls import path
from .views import sign_up, log_in, dashboard
from .views import log_out, view_units, base
from . import views


urlpatterns = [
    path('sign_up', sign_up, name='sign_up'),
    path('', views.homepage, name='homepage'),
    path('log_in/', log_in, name='log_in'),
    path('dashboard/', dashboard, name='dashboard'),
    path('log_out/', log_out, name='log_out'),
    path('view_units/', view_units, name='view_units'),
    path('base/', base, name='base'),
    path('fees/', views.school_fees_status, name='school_fees_status'),  # Link to school fees status page



]

