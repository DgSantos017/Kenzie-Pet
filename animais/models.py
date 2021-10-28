from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField() 
    weight = models.FloatField()  
    sex = models.CharField(max_length=255)

class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    animais = models.ForeignKey("Animal", on_delete=models.CASCADE)

class Characteristic(models.Model):
    name = models.CharField(max_length=255)
    animais = models.ManyToManyField(Animal)
