from django.urls import path
from . import views

urlpatterns = [
    path('parentsignin', views.parent_sign_in, name='parent_sign_in'),
    path('parent_dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('student/<int:student_id>/', views.student_information, name='student_information'),
    path('parent_messages/<int:student_id>/', views.parent_messages, name='parent_messages'),

]
