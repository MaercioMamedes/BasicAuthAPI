from django.contrib.auth.models import User
from django.db import models


class UserApp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField('Nome Completo', max_length=200)

    def __str__(self):
        return self.fullname