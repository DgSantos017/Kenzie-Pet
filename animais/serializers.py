from rest_framework import serializers

class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    grupo = serializers.CharField() 
    