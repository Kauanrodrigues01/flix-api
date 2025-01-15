import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Rating cannot be less than 0 stars.'),
            MaxValueValidator(5, 'Rating cannot be higher than 0 stars.')
        ]
    )
    comment = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{str(self.movie)} | starts: {self.stars}'