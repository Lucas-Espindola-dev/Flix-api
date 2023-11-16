from django.urls import path
from movies.views import MoviesCreateListView, MoviesRetrieveUpdateDestroyView


urlpatterns = [
    path('movies/', MoviesCreateListView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MoviesRetrieveUpdateDestroyView.as_view(), name='movies-detail-view'),
]
