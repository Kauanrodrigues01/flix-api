from rest_framework import generics
from .models import Actor
from movies.models import Movie
from .serializers import ActorSerializer
from rest_framework.exceptions import NotFound

class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    def filter_queryset(self, queryset):
        name = self.request.query_params.get('name', None)
        movie_id = self.request.query_params.get('movie', None)
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        
        if movie_id:
            try:
                movie = Movie.objects.get(pk=movie_id)
            except Movie.DoesNotExist:
                raise NotFound(detail="Movie not found.")
            
            queryset = queryset.filter(id__in=movie.actors.values_list('id', flat=True))
        
        return super().filter_queryset(queryset)


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer