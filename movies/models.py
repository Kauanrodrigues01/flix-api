import uuid

from django.db import models

from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    resume = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
