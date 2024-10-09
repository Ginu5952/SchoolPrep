from rest_framework import serializers
from apps.Parent.models.parent import Parent
from apps.User.serializer.user import UserSerializer

class ParentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()  

    class Meta:
        model = Parent
        fields = ['id', 'user', 'address', 'phone_number', 'gender']  