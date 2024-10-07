# serializers.py

from rest_framework import serializers
from apps.Parent.models.writemsg import Write_msg
from apps.Parent.models.parent import Parent
from apps.Student.models.student import Student
from apps.Teacher.models.teacher import Teacher

class WriteMsgSerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(queryset=Parent.objects.all(), source='parent')
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student')
    teacher_id = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all(), source='teacher')

    parent_name = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Write_msg  
        fields = ['id', 'parent_id', 'parent_name', 'student_id', 'student_name', 'teacher_id', 'teacher_name', 'text_msg','response']
        
    def get_parent_name(self, obj):
        return f"{obj.parent.user.first_name} {obj.parent.user.last_name}"
    
    def get_teacher_name(self, obj):
        return f"{obj.teacher.user.first_name} {obj.teacher.user.last_name}"

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"

    def validate_text_msg(self, value):
        if not value:
            raise serializers.ValidationError("Message text cannot be empty.")
        return value

    def create(self, validated_data):
        return Write_msg.objects.create(**validated_data)
