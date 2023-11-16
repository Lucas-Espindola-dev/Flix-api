from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('genres.urls')),
    # path('', include('actors.urls')),
]
