from rest_framework import serializers
from .models import User, Profile
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['kakaoid']

    def validate(self, attrs):
        kakaoid = attrs.get('kakaoid', '')

        if User.objects.filter(kakaoid=kakaoid).exists():
            raise serializers.ValidationError('Already existing Kakao ID')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    kakaoid = serializers.CharField(max_length=250, min_length=3)
    password = serializers.CharField(max_length=25, min_length=4, default='1111')
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):

        user = User.objects.get(kakaoid=obj['kakaoid'])

        return{
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['kakaoid', 'password', 'tokens']

    def validate(self, attrs):
        kakaoid = attrs.get('kakaoid', '')
        password = attrs.get('password', '1111')

        user = auth.authenticate(kakaoid=kakaoid, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials')

        return {
            'kakaoid': user.kakaoid,
            'tokens': user.tokens()
        }


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
