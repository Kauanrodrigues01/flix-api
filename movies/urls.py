from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListCreateView.as_view(), name='movies-list-create'),
    path('<uuid:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movies-retrieve-update-destroy')
]