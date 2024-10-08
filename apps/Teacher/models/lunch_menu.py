from django.db import models
from apps.Teacher.models.timetable import TimeTable

class LunchMenu(models.Model):
    week = models.DateField()
    lunch_menu = models.JSONField()
    timetable = models.ForeignKey(TimeTable, on_delete=models.SET_NULL,null=True)
 
    def __str__(self):
        return f"LunchMenu for {self.week}"