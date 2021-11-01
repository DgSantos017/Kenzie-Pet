from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from animais.serializers import AnimalSerializer, GroupSerializer, CharacteristicSerializer
from datetime import datetime
from .models import Animal, Characteristic, Group
from django.core.exceptions import ObjectDoesNotExist


class AnimalView(APIView):
    
    def post(self, request):
        data = request.data
        request_group = data.pop('group')
        characteristics = data.pop('characteristics')

        group = Group.objects.filter(scientific_name=request_group['scientific_name'])
        
        if not group:
            group = Group(name=request_group['name'], scientific_name=request_group['scientific_name'])
            group.save()

        group = Group.objects.get(scientific_name=request_group['scientific_name'])

        animal = Animal(name=data['name'], age=data['age'], weight=data['weight'], sex=data['sex'], group=group)
        animal.save()

        for characteristic in characteristics:
            animal_characteristic = Characteristic.objects.filter(name=characteristic['name'])

            if not animal_characteristic:
                animal_characteristic = Characteristic(name=characteristic['name'])
                animal_characteristic.save()
            
            animal_characteristic = Characteristic.objects.get(name=characteristic['name'])

            animal.characteristics.add(animal_characteristic)
            animal.save()

        animal = Animal.objects.get(pk=animal.id)
        serializer = AnimalSerializer(animal)

        if serializer:
            return Response(serializer.data, status=201)
        return Response(serializer.errors)


    def get(self, request, animal_id=''):
        if animal_id:
            try:
                animais = Animal.objects.get(id=animal_id)
                serializer = AnimalSerializer(animais)
                return Response(serializer.data, status=200)

            except ObjectDoesNotExist:
                return Response({'error': 'Animal not found'}, status=404)

        animais = Animal.objects.all()
        serializer = AnimalSerializer(animais, many=True)
        return Response(serializer.data, status=200)



    def delete(self, request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)
            animal.delete()
            return Response(status=204)

        except ObjectDoesNotExist:
            return Response({'error': 'Animal not found'}, status=404)

