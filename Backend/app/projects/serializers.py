from dataclasses import fields
from rest_framework import serializers
from .models import Project
#Clase con los datos correspondiente al listado en base de datos
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)