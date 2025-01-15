from django.urls import path
from . import views

app_name = 'actors'

urlpatterns = [
    path('', views.ActorListCreateView.as_view(), name='actors-list-create'),
    path('<uuid:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actors-retrieve-update-destroy'),
]