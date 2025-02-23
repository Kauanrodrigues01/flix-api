from datetime import datetime
from collections import defaultdict

from django.db.models import Avg
from rest_framework import serializers

from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer
from .models import Movie


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        try:
            average_stars = obj.reviews.aggregate(average_stars=Avg('stars'))['average_stars']

            if average_stars is None:
                return 0
            return round(average_stars, 2)

        except Exception as e:
            print(f"Unexpected error while calculating rate: {e}")
            return 0


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        try:
            average_stars = obj.reviews.aggregate(average_stars=Avg('stars'))['average_stars']

            if average_stars is None:
                return 0
            return round(average_stars, 2)

        except Exception as e:
            print(f"Unexpected error while calculating rate: {e}")
            return 0

    def validate(self, data):
        title = data.get('title', None)
        release_date = data.get('release_date', None)
        resume = data.get('resume', None)
        current_date = datetime.today().date()
        errors = defaultdict(list)

        if title:
            if Movie.objects.filter(title__iexact=title).exists():
                errors['title'].append('Título já existe')
            if len(title) < 3:
                errors['title'].append('Título deve ter pelo menos 3 caracteres')

        if release_date:
            if release_date > current_date:
                errors['release_date'].append(f'Data de lançamento não pode ser no futuro. Data atual: {current_date.strftime('%Y-%m-%d')}')

        if resume:
            if len(resume) < 10:
                errors['resume'].append('O resumo deve ter pelo menos 10 caracteres')

        if errors:
            raise serializers.ValidationError(errors)

        return data
