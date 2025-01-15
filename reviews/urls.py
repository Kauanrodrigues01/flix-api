from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('reviews/', views.ReviewListCreate.as_view(), name='reviews-list-create'),
    path('reviews/<uuid:pk>/', views.ReviewRetrieveUpdateDestroy.as_view(), name='reviews-retrieve-update-destroy')
]
