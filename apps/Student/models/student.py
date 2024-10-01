
from django.db import models
from apps.Parent.models.parent import Parent

class Student(models.Model):
    
  
    
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE) 
    parent =  models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)  
    age = models.PositiveIntegerField()
    # class_id = models.ForeignKey(Class, on_delete=models.CASCADE) 
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)  
    first_name = models.CharField(max_length=100, null=True, blank=True)  
    last_name = models.CharField(max_length=100, null=True, blank=True)  
   