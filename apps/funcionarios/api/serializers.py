from rest_framework import serializers

from apps.funcionarios.models import Funcionario


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome', 'departamentos', 'empresa', 'user', 'imagem')
        # fields = ('nome', 'departamentos', 'empresa', 'user', 'imagem')
