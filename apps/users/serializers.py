# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_uuid', 'name', 'email', 'password']

        # Siginifica que o campo de 'password' será exibido apenas para escrita e não mais como 
        # retorno para vizualização
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
