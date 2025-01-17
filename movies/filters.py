from django_filters import rest_framework as filters
from .models import Movie
from genres.models import Genre
from actors.models import Actor


class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    genre = filters.ModelChoiceFilter(queryset=Genre.objects.all().only('id'))
    release_date = filters.DateFromToRangeFilter(field_name='release_date')
    release_year = filters.NumberFilter(field_name='release_date', lookup_expr='year')
    actors = filters.ModelMultipleChoiceFilter(queryset=Actor.objects.all().only('id'))

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'release_date', 'actors']
