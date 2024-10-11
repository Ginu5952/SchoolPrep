from django.db import models
from apps.Student.models.student import student 
from apps.Teacher.models.teacher import Teacher
from django.utils import timezone


class Attendance(models.Model):
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    date = models.DateField(default=timezone.now)
    is_present = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.date} --> {self.student} --> {'Present' if self.is_present else 'Absent'}"