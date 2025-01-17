from rest_framework import serializers
from .models import Actor
from collections import defaultdict
from datetime import datetime


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate(self, data):
        name = data.get('name', None)
        birthday = data.get('birthday', None)
        current_date = datetime.today().date()
        current_date_str = current_date.strftime('%Y-%m-%d')
        errors = defaultdict(list)

        if name:
            if Actor.objects.filter(name__iexact=name).exists():
                errors['name'].append('Name already exists')
            if len(name) < 3:
                errors['name'].append('Name should be at least 3 characters long')

        if birthday:
            if birthday > current_date:
                errors['birthday'].append(f'Birthday cannot be in the future. Current date: {current_date_str}')

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['nationality'] = instance.get_nationality_display()
        return data
