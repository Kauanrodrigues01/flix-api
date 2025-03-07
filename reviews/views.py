from rest_framework import generics
from rest_framework.exceptions import NotFound

from movies.models import Movie
from utils.pagination import create_pagination_class

from .models import Review
from .permissions import ReviewPermission
from .serializers import ReviewSerializer

Pagination = create_pagination_class(page_size=30, page_size_query_param='page_size', max_page_size=100)


class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = Pagination
    permission_classes = [ReviewPermission,]

    def filter_queryset(self, queryset):
        movie_id = self.request.query_params.get('movie', None)
        stars = self.request.query_params.get('stars', None)
        stars_min = self.request.query_params.get('stars_min', None)
        stars_max = self.request.query_params.get('stars_max', None)

        if movie_id:
            try:
                movie = Movie.objects.get(pk=movie_id)
            except Movie.DoesNotExist:
                raise NotFound(f'Movie with id {movie_id} not found')

            queryset = queryset.filter(movie=movie)

        if stars_min:
            try:
                stars_min = int(stars_min)
                queryset = queryset.filter(stars__gte=stars_min)
            except ValueError:
                raise NotFound(f'Invalid value for stars_min: {stars_min}')

        if stars_max:
            try:
                stars_max = int(stars_max)
                queryset = queryset.filter(stars__lte=stars_max)
            except ValueError:
                raise NotFound(f'Invalid value for stars_max: {stars_max}')

        if stars:
            try:
                stars = int(stars)
                queryset = queryset.filter(stars=stars)
            except ValueError:
                raise NotFound(f'Invalid value for stars: {stars}')

        return queryset


class ReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewPermission,]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or not user.is_authenticated or self.request.method == 'GET':
            return self.queryset
        return Review.objects.filter(user=user)
