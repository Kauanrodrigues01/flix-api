from django.db.models import Count, Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, views, response, status

from app.permissions import GlobalDefaultModelPermission
from utils.pagination import create_pagination_class
from reviews.models import Review
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
    permission_classes = [GlobalDefaultModelPermission]


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.prefetch_related('actors').all()
    serializer_class = MovieSerializer
    permission_classes = [GlobalDefaultModelPermission]

    def destroy(self, request, *args, **kwargs):
        movie = self.get_object()
        if movie.reviews.exists():
            return response.Response(
                {'error': 'Cannot delete movie with related reviews.'},
                status=status.HTTP_502_BAD_GATEWAY
            )
        return super().destroy(request, *args, **kwargs)


class MovieStatsView(views.APIView):
    queryset = Movie.objects.select_related('genre').prefetch_related('actors').all()
    permission_classes = [GlobalDefaultModelPermission]

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(average_stars=Avg('stars'))['average_stars']

        return response.Response(
            data={
                'total_movies': total_movies,
                'movies_by_genre': list(movies_by_genre),
                'total_reviews': total_reviews,
                'average_stars': round(average_stars, 2) if average_stars else 0,
            },
            status=200
        )
