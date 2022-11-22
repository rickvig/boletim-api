from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import *

from .models import Aluno


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all().order_by('nome')
    serializer_class = AlunoSerializer
    permission_classes = [permissions.IsAuthenticated]    
    
    
class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all().order_by('nome')
    serializer_class = DisciplinaSerializer
    permission_classes = [permissions.IsAuthenticated]      
    
    
class BoletimViewSet(viewsets.ModelViewSet):
    queryset = Boletim.objects.all().order_by('data_entrega')
    serializer_class = BoletimSerializer
    permission_classes = [permissions.IsAuthenticated]  
    
    
class BoletimNotaViewSet(viewsets.ModelViewSet):
    queryset = BoletimNota.objects.all().order_by('boletim')
    serializer_class = BoletimNotaSerializer
    permission_classes = [permissions.IsAuthenticated]          
        