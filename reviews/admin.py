from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'stars', 'comment')
    search_fields = ('movie__title', 'comment')
    list_filter = ('stars',)