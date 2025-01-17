from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MovieFilter
from utils.pagination import create_pagination_class

Pagination = create_pagination_class(page_size=30, page_size_query_param='page_size', max_page_size=100)


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.select_related('genre').prefetch_related('actors').all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter
    pagination_class = Pagination


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.prefetch_related('actors').all()
    serializer_class = MovieSerializer
