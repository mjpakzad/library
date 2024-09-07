from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            return user
        elif not user:
            user = User.objects.create_user(email=email, password=password)
            return user
        raise serializers.ValidationError("Invalid credentials")
