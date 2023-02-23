from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "email", "password", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        is_superuser = validated_data.pop("is_superuser", None)

        if is_superuser:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        is_superuser = validated_data.pop("is_superuser", None)
        if is_superuser:
            raise PermissionDenied("Superuser property cannot be changed.")

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
