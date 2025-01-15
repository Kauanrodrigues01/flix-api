from django.urls import path
from . import views

app_name = 'genres'

urlpatterns = [
    path('genres/', views.GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<uuid:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-retrieve-update-destroy')
]