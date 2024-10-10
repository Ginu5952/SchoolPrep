from rest_framework import serializers
from apps.Teacher.models.teacher import Teacher, Class
from apps.User.serializer import UserSerializer

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name', 'academic_year_start', 'academic_year_end', 'grade','teacher_id']


class TeacherSerializer(serializers.ModelSerializer):
    
    user = UserSerializer() 
    
    class Meta:
        model = Teacher
        fields = ["id", "user", "gender",]
        

    def create(self, validated_data):
        user_data = validated_data.pop('user')  
       
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()  
       
       
        teacher = Teacher.objects.create(user=user, **validated_data)

        return teacher


