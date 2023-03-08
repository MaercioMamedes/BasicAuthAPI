from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from core.serializers import AccountSerializer
from core.models import Account


"""Classe View para acessar saldo e realizar transações do caixa do usuário logado"""


class OperationView(GenericAPIView):
    serializer_class = AccountSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        account_user = Account.objects.filter(user=self.request.user.id).first()
        return Response(
            {
                'usuario': user.username,
                'saldo': account_user.balance,
            }
        )

    def post(self, request):
        user = self.request.user
        account_user = Account.objects.filter(user=self.request.user.id).first()
        data = self.get_serializer(data=request.data)
        data.is_valid(raise_exception=True)

        if data.is_valid():
            operation = data.validated_data['operation_field']
            print(operation)
            value_operation = data.validated_data['value_operation']

            if operation == 'saque':
                account_user.to_withdraw(value_operation)
                account_user.save()
                return Response(
                    {
                        'mensagem': 'saque realizado com sucesso',
                        'usuario': user.username,
                        'saldo': f'{account_user.balance}',
                    }
                )

            elif operation == 'deposito':
                account_user.to_deposit(value_operation)
                account_user.save()
                return Response(
                    {
                        'mensagem': 'depósito realizado com sucesso',
                        'usuario': user.username,
                        'saldo': f'{account_user.balance}',
                    }
                )
