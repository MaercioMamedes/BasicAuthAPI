from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField('saldo', max_digits=10, decimal_places=2, default=0)

    def to_withdraw(self, value):

        if value < 0:
            raise ValueError('O valor do saque não pode ser negativo')
        elif self.balance < value:
            raise ValueError('Saldo insufiente')
        else:
            self.balance -= value

    def to_deposit(self, value):

        if value < 0:
            raise ValueError('O valor do saque não pode ser negativo')

        else:
            self.balance += value
