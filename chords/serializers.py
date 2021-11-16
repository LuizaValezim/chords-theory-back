from rest_framework import serializers
from .models import Combinations

class CombinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combinations
        fields = ['id', 'chords']