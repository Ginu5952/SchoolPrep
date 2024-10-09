from rest_framework import serializers
from apps.Teacher.models.timetable import TimeTable

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta : 
        model= TimeTable
        fields = '__all__'
 
