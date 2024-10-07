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
    

admin.site.register(Teacher)
admin.site.register(Class, ClassAdmin)


# Register your models here.
