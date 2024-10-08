
from rest_framework import serializers
from apps.Student.models.student import Student, Announcement
#from apps.teacher.serializer.classs import ClassSerializer
from django.contrib.auth.models import User
from apps.Teacher.models.teacher import Class
from django.contrib.auth.hashers import check_password

class StudentSerializer(serializers.ModelSerializer):
    
    #class_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())  
    #class_info = ClassSerializer(source='class_id', read_only=True) 
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    

    class Meta:
        model = Student
        fields = ['id','first_name','last_name','username','password']
  

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'date', 'teacher_id', 'class_id']
