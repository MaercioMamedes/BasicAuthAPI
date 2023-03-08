from rest_framework import serializers
from core.models import Account
"""Classe que representa o caixa do usuário"""


class AccountSerializer(serializers.Serializer):
    operation = (
        ('saque','saque'),
        ('deposito','deposito')

    )
    operation_field = serializers.ChoiceField(label='Operação', choices=operation)
    value_operation = serializers.DecimalField(label='Valor', max_digits=8, decimal_places=2)

    def validate(self, attrs):
        return attrs
