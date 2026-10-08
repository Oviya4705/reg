from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):

        password = validated_data.get('password')

        if password:
            validated_data['password'] = make_password(password)

        return Registration.objects.create(
            **validated_data
        )

    def update(self, instance, validated_data):

        password = validated_data.get('password')

        if password:
            validated_data['password'] = make_password(password)

        return super().update(
            instance,
            validated_data
        )