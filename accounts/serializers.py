from rest_framework import serializers

from content.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'first_name', 'last_name')


