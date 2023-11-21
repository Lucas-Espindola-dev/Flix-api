from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('genres.urls')),
    path('', include('actors.urls')),
    path('', include('movies.urls')),
    path('', include('reviews.urls')),
]
