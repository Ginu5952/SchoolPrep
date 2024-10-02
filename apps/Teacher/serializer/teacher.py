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
