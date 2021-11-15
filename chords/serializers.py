from rest_framework import serializers
from .models import Combinations

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combinations
        fields = ['id','title', 'chords']