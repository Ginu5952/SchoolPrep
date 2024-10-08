from rest_framework import serializers
from apps.Teacher.models.timetable import TimeTable

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta : 
        model= TimeTable
        firleds = ['id', 'teacher', 'class_id', 'timetable_content']
 
