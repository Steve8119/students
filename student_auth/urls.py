from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('parents/', include('parents.urls')),
    path('administration/', include('administration.urls')),
]
