from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date')
    search_fields = ('title', 'genre__name')
    list_filter = ('genre', 'release_date')
    filter_horizontal = ('actors',)
    ordering = ('-release_date',)