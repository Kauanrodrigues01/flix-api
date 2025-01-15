from django.urls import path
from . import views

urlpatterns = [
    path('', views.GenreListCreateView.as_view(), name='genre_list'),
]