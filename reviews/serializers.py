from rest_framework import serializers
from .models import Review
from collections import defaultdict


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        
    def validate(self, data):
        movie = data.get('movie', None)
        comment = data.get('comment', None)
        request_method = self.context['request'].method
        errors = defaultdict(list)
        
        if request_method in ['PUT', 'PATCH']:
            if movie:
                errors['movie'].append('You cannot change the movie for an existing review.')
        
        if comment:
            if len(comment) < 3:
                errors['comment'].append('Comment must be at least 3 characters long.')
                
        if errors:
            raise serializers.ValidationError(errors)
            
        return data