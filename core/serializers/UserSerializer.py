from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','username', 'password']
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        """Método para criar usuário"""
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            username=validated_data['username'],
            password=validated_data['password'],
        )

        Account.objects.create(user=user)  # cria carteira do usuário

        return user






