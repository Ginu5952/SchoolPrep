
from django.db import models
from apps.Parent.models.parent import Parent
from apps.Teacher.models.teacher import Class, Teacher


class Student(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE) 
    parent =  models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)  
    age = models.PositiveIntegerField()
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE,default = 1) 
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)  
    first_name = models.CharField(max_length=100, null=True, blank=True)  
    last_name = models.CharField(max_length=100, null=True, blank=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Announcement(models.Model):
    title = models.CharField(max_length=50, null= True, blank= True)
    content = models.TextField(null= True,blank= True)
    date = models.DateTimeField(auto_now_add= True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, null= True, blank= True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, null= True, blank= True)

    def __str__(self):
        return f"{self.title} on {self.date}"
    