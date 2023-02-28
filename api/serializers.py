from rest_framework import serializers

class Student(serializers.Serializer):
    nombre = serializers.CharField()
    matricula = serializers.CharField()

class Teacher(serializers.Serializer):
    id = serializers.IntegerField()
    numeroEmpleado = serializers.IntegerField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    horasClase = serializers.IntegerField()