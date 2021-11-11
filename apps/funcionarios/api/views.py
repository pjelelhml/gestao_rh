from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.funcionarios.api.serializers import FuncionarioSerializer
from apps.funcionarios.models import Funcionario


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = FuncionarioSerializer
