from rest_framework import generics, status
from genres.models import Genre
from genres.serializers import GenreSerializer
from django.http import JsonResponse


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

    def destroy(self, request, *args, **kwargs):
        genre = self.get_object()
        if genre.movies.exists():
            return JsonResponse(
                {'error': 'Cannot delete genre with related movies.'},
                status=status.HTTP_502_BAD_GATEWAY
            )

        return super().destroy(request, *args, **kwargs)
