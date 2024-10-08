from django.contrib import admin
from apps.Teacher.models.teacher import Teacher, Class


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "class_name",
        "academic_year_start",
        "academic_year_end",
        "grade",
        "teacher_id"
    )

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'first_name', 'last_name', 'gender')

    def username(self, obj):
        return obj.user.username  

    def first_name(self, obj):
        return obj.user.first_name  

    def last_name(self, obj):
        return obj.user.last_name  


    username.admin_order_field = 'user__username'  
    first_name.admin_order_field = 'user__first_name'  
    last_name.admin_order_field = 'user__last_name'  
       

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Class, ClassAdmin)


# Register your models here.
