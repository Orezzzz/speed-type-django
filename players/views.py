from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from players.models import Players
from players.serializers import playersSerializers

# Create your views here.

@csrf_exempt
def playersApi(request,id=0):
    if request.method=='GET':
        players = Players.objects.all()
        players_serializers = playersSerializers(players, many=True)
        return JsonResponse(players_serializers.data, safe=False)
    elif request.method=='POST':
        players_data = JSONParser().parse(request)
        players_serializers = playersSerializers(data = players_data)
        if players_serializers.is_valid():
            players_serializers.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        players_data = JSONParser().parse(request)
        players = Players.objects.get(name=players_data["name"], password=players_data["password"])
        players_serializers = playersSerializers(players, data = players_data)
        if players_serializers.is_valid():
            players_serializers.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)