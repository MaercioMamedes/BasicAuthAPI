from rest_framework import viewsets
from core.serializers import UserSerializer
from django.contrib.auth.models import User


class UserAppView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
