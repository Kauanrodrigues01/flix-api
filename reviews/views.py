from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from movies.models import Movie
from rest_framework.exceptions import NotFound

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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