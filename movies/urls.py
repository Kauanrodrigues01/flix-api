from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('movies/', views.MovieListCreateView.as_view(), name='movies-list-create'),
    path('movies/<uuid:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movies-retrieve-update-destroy'),
    path('movies/stats/', views.MovieStatsView.as_view(), name="movie-stats-view")
]
