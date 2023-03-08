from rest_framework import viewsets
from core.serializers import UserSerializer
from django.contrib.auth.models import User


class UserAppView(viewsets.ModelViewSet):
    serializer_class = UserSerializer


    def get_queryset(self):

        return User.objects.filter(id=self.request.user.id)


