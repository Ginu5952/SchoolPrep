
from rest_framework import serializers
from apps.Student.models.student import Student
from apps.Teacher.serializer.teacher import ClassSerializer
from django.contrib.auth.models import User
from apps.Teacher.models.teacher import Class
from django.contrib.auth.hashers import check_password

class StudentSerializer(serializers.ModelSerializer):
    
    class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())  
    class_info = ClassSerializer(source='class_id', read_only=True) 
    #teacher_name = serializers.CharField(source='teacher.user.first_name', read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    #class_id1 = ClassSerializer()
    

    class Meta:
        model = Student
        fields = ['id','first_name','last_name', 'age', 'class_id', 'class_info', 'gender','username','password']
  
  