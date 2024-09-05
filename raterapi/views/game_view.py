from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from raterapi.models import Game
from django.contrib.auth.models import User

class GameView(ViewSet):
    def list (self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve (self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)




class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ( 'id', 'title', 'description', 'designer', 'year_released', 'number_of_players', 'estimated_play_time', 'age_recommendation', 'user', 'categories')