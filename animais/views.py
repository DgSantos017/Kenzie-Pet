from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Animal, Group, Characteristic
from animais.serializers import AnimalSerializer

class AnimalView(APIView):
    def get(self, request):
        animais = Animal.objects.all()

        serialized = AnimalSerializer(animais, many=True)

        return Response(serialized.data)
