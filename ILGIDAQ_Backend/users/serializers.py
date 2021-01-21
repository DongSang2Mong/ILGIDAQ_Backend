from rest_framework import serializers
from .models import UserLoginInfo, UserProfile

### 얘도 알아서 편집 ###

class UserLoginInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserLoginInfo
        fields = '__all__'


###

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'