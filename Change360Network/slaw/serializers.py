from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Nominees


class NomineeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nominees
        exclude = ['is_approved', 'votes']


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password',
            'is_superuser',
            'is_staff',
            'is_active',
            'user_permissions'
        ]
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


        