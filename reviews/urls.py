from django.urls import path
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView


urlpatters = [
    path('reviews/', ReviewCreateListView.as_view(), name='reviews-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='reviews-detail-view'),
]
