
from django.db import models



class Class(models.Model):    
    class_name = models.CharField(max_length=100)
    academic_year_start = models.IntegerField()
    academic_year_end = models.IntegerField()
    grade = models.IntegerField()        



class Teacher(models.Model):
    
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE) 
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE,default = 1)  
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


