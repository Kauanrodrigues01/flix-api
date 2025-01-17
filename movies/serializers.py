from rest_framework import serializers
from .models import Movie
from collections import defaultdict
from datetime import datetime


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate(self, data):
        title = data.get('title', None)
        release_date = data.get('release_date', None)
        resume = data.get('resume', None)
        current_date = datetime.today().date()
        errors = defaultdict(list)

        if title:
            if Movie.objects.filter(title__iexact=title).exists():
                errors['title'].append('Title already exists')
            if len(title) < 3:
                errors['title'].append('Title should be at least 3 characters long')

        if release_date:
            if release_date > current_date:
                errors['release_date'].append(f'Release date cannot be in the future. Current date: {current_date.strftime('%Y-%m-%d')}')

        if resume:
            if len(resume) < 10:
                errors['resume'].append('The resume must be at least 10 characters long.')

        if errors:
            raise serializers.ValidationError(errors)

        return data
