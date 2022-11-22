from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        

class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'data_nascimento']
        
        
class DisciplinaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['nome', 'carga_horaria']       
        
class BoletimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boletim
        fields = ['aluno', 'data_entrega']  
        
class BoletimNotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoletimNota
        fields = ['nota', 'disciplina', 'boletim']                   
