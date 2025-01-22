from rest_framework import generics
from .models import Actor
from movies.models import Movie
from .serializers import ActorSerializer
from rest_framework.exceptions import NotFound
from utils.pagination import create_pagination_class
from rest_framework.permissions import AllowAny, IsAdminUser

Pagination = create_pagination_class(page_size=30, page_size_query_param='page_size', max_page_size=100)


class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = Pagination

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

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        return [IsAdminUser()]


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        return [IsAdminUser()]
