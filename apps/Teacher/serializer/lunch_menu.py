from rest_framework import serializers
from apps.Teacher.models.lunch_menu import LunchMenu



class LunchMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = LunchMenu
        fields = ['timetable','Week', 'lunch_menu' ]
