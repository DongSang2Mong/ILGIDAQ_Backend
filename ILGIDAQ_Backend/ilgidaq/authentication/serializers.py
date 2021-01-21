from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    userid = serializers.CharField(max_length=250)

    class Meta:
        model = User
        fields = ['userid']

    def validate(self, attrs):
        userid = attrs.get('userid', '')

        if not userid.isalnum():
            raise serializers.ValidationError('The user ID should only contain alphanumeric characters.')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    userid = serializers.CharField(max_length=250)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):

        user = User.objects.get(userid=obj['userid'])

        return {
            'access': user.tokens()['access'],
            'refresh': user.tokens()['refresh']
        }

    class Meta:
        model = User
        fields = ['userid', 'tokens']

    def validate(self, attrs):
        userid = attrs.get('userid', '')

        user = auth.authenticate(userid=userid)

        if not user:
            raise AuthenticationFailed('Invalid credentials')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        return{
            'userid': user.userid,
            'tokens': user.tokens()
        }

