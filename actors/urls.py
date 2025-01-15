from django.urls import path
from . import views

app_name = 'actors'

urlpatterns = [
    path('actors/', views.ActorListCreateView.as_view(), name='actors-list-create'),
    path('actors/<uuid:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actors-retrieve-update-destroy'),
]