from rest_framework import serializers
from apps.Parent.models.parent import Parent
from apps.User.serializer.user import UserSerializer
from django.contrib.auth.models import User

class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Parent
        fields = ['user', 'address', 'phone_number', 'gender', 'children']

    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'],
            first_name=user_data.get('first_name', ''),
            last_name=user_data.get('last_name', ''),
            email=user_data.get('email', '')
        )
       

        parent = Parent.objects.create(
        user=user,
        phone_number=validated_data.get('phone_number'),
        address=validated_data.get('address'),
        gender=validated_data.get('gender')
        )
          
        return parent    