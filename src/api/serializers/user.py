""" Authentication serializers"""

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from src.api.models import User, Company
from src.api.helpers.user import get_jwt_token


class RegistrationSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(RegistrationSerializer, self).__init__(*args, **kwargs)

        """
        Add custom error messages
        """
        for field in self.fields:
            error_messages = self.fields[field].error_messages
            error_messages['null'] = error_messages['blank'] \
                = error_messages['required'] \
                = 'Please supply your {}.'.format(field)
    username = serializers.RegexField(
        regex='^[A-Za-z\-\_]+\d*$',
        min_length=3,
        max_length=20,
        required=True,
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='The username already exists. Kindly try another.'
        )],
        error_messages={
            'min_length': 'Username allows a minimum of 3 characters.',
            'max_length': 'Username allows a maximum of 20 characters.',
            'invalid': 'Username should contain alphanumeric characters.'
        }
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='Email already exists. '
                    'Please enter another email or sign in.'
        )],
        error_messages={
            'invalid': 'Please enter a valid email address.'
        }
    )
    password = serializers.RegexField(
        regex=r'^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[\!\@#\$%\^&]).*',
        max_length=128,
        min_length=8,
        write_only=True,
        error_messages={
            'max_length': 'Password allows a maximum of 128 characters.',
            'min_length': 'Password allows a minimum of 8 characters.',
            'invalid': 'Password must contain at least 1 letter, '
                       'a number and a special character.',
        })
    token = serializers.SerializerMethodField()
    company = serializers.CharField(max_length=50)

    def get_token(self, obj):
        token = get_jwt_token(obj)
        return token

    class Meta:
        model = User
        fields = ['email', 'token', 'password', 'company', 'username']

    def create(self, validated_data):
        company_name = validated_data.pop('company')
        try:
            company = Company.objects.get(name=company_name)
        except Company.DoesNotExist as BaseException:
            raise serializers.ValidationError('Company does not exist')
        return User.objects.create_user(company=company, **validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError('Wrong email or password.')
        data['token'] = get_jwt_token(user)
        return data
