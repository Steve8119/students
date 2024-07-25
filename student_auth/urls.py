# student_auth/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),  # Ensure this matches your app's URLs
    path('parents/', include('parents.urls')),  # Ensure this matches your app's URLs
    path('administration/', include('administration.urls')),  # Ensure this matches your app's URLs
]
