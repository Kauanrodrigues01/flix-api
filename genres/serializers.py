from rest_framework import serializers
from genres.models import Genre
from collections import defaultdict

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
    def validate(self, data):
        name = data.get('name', '')
        errors = defaultdict(list)
        
        if Genre.objects.filter(name__iexact=name).exists():
            errors['name'].append('Name already exists')
        if len(name) < 3:
            errors['name'].append('Name should be at least 3 characters long')
            
        if errors:
            raise serializers.ValidationError(errors)
        
        return data