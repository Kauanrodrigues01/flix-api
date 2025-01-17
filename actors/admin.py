from django.contrib import admin
from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('nationality',)
