from collections import defaultdict
from rest_framework import serializers
from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

    def validate(self, data):
        name = data.get('name', '')
        errors = defaultdict(list)

        if Genre.objects.filter(name__iexact=name).exists():
            errors['name'].append('Nome já existe')
        if len(name) < 3:
            errors['name'].append('Nome deve ter pelo menos 3 caracteres')

        if errors:
            raise serializers.ValidationError(errors)

        return data
