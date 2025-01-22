from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response

from app.permissions import ModelPermission
from utils.pagination import create_pagination_class
from .filters import MovieFilter
from .models import Movie
from .serializers import MovieSerializer

Pagination = create_pagination_class(page_size=30, page_size_query_param='page_size', max_page_size=100)


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.select_related('genre').prefetch_related('actors').all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter
    pagination_class = Pagination
    permission_classes = [ModelPermission]


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.prefetch_related('actors').all()
    serializer_class = MovieSerializer
    permission_classes = [ModelPermission]

    def destroy(self, request, *args, **kwargs):
        movie = self.get_object()
        if movie.reviews.exists():
            return Response(
                {'error': 'Cannot delete movie with related reviews.'},
                status=status.HTTP_502_BAD_GATEWAY
            )
        return super().destroy(request, *args, **kwargs)
