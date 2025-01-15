from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    def filter_queryset(self, queryset):
        name = self.request.query_params.get('name', None)
        
        if name:
           return queryset.filter(name__icontains=name)
        
        return super().filter_queryset(queryset)
    
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer