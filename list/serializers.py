from rest_framework import serializers
from .models import GameInstance


class GameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GameInstance
        fields = ('user','title','platform')
