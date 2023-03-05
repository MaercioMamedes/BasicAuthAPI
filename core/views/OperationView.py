from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from core.serializers import AccountSerializer
from core.models import Account


class OperationView(GenericAPIView):
    serializer_class = AccountSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        account_user = Account.objects.get(user=self.request.user)
        return Response({'saldo': account_user.balance})

    def post(self, request):
        account_user = Account.objects.get(user=self.request.user)
        print(self.request.data)
        data = self.serializer_class(data=self.request.data)

        if data.is_valid:
            if data.operation_field == 'withdraw':
                account_user.to_withdraw(data.value_operation)
                account_user.save()
                return Response(
                    {
                        'mensagem': 'saque realizado com sucesso',
                        'saldo': f'{account_user.balance}',
                    }
                )

            elif data.operation_field == 'deposit':
                account_user.to_deposit(data.value_operation)
                account_user.save()
                return Response(
                    {
                        'mensagem': 'depósito realizado com sucesso',
                        'saldo': f'{account_user.balance}',
                    }
                )
