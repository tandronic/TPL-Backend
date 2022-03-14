from django.contrib.auth import password_validation as validators
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from user.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password_2')

    def validate(self, data):
        if User.objects.filter(email=data['email']).first():
            raise serializers.ValidationError("This email is already used.")
        if data['password'] != data['password_2']:
            raise serializers.ValidationError("Password and password_2 fields have not same values.")

        new_data = data.copy()
        new_data.pop('password_2')
        user = User(**new_data)

        # get the password from the data
        password = data.get('password')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=User)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        return super(RegisterSerializer, self).validate(data)

    def save(self, **kwargs):
        self.validated_data['password'] = make_password(self.validated_data['password'])
        return super(RegisterSerializer, self).save(**kwargs)


class ActivateSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=64)
    token = serializers.CharField(max_length=256)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=50)
    new_password = serializers.CharField(max_length=50)
    new_password_2 = serializers.CharField(max_length=50)

    def validate(self, data):
        if data['new_password'] != data['new_password_2']:
            raise serializers.ValidationError("new_password and new_password_2 fields have not same values.")

        # get the password from the data
        password = data.get('new_password')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=User)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['new_password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        return super(ChangePasswordSerializer, self).validate(data)
