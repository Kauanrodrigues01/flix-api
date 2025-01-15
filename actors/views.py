from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer

class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    def filter_queryset(self, queryset):
        name = self.request.query_params.get('name', None)
        
        if name:
            return queryset.filter(name__icontains=name)
        
        return super().filter_queryset(queryset)


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer