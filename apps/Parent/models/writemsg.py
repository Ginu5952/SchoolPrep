from django.db import models
from apps.Parent.models.parent import Parent  
from apps.Student.models.student import Student 
from apps.Teacher.models.teacher import Teacher


class Write_msg(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name="Sender Parent")  
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student Involved")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Recipient Teacher")
    text_msg = models.TextField(verbose_name="Message Text")
    response = models.TextField(verbose_name="Teacher Response", blank=True, null=True)

    def __str__(self):
        return f"Message from {self.parent} to {self.teacher} about {self.student} - {self.text_msg[:20]}..."
