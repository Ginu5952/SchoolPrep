from django.contrib import admin
from apps.Teacher.models.teacher import Teacher, Class
from apps.Teacher.models.lunch_menu import LunchMenu
from apps.Teacher.models.timetable import TimeTable


class ClassAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "class_name",
        "academic_year_start",
        "academic_year_end",
        "grade",
        "teacher_id",
    )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "gender")

    def username(self, obj):
        return obj.user.username

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    username.admin_order_field = "user__username"
    first_name.admin_order_field = "user__first_name"
    last_name.admin_order_field = "user__last_name"


"""       
class TimeTableAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "class", 
        "teacher",  
        "timetable_content",
    )


class LunchMenuAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "week", 
        "timetable",  
        "lunch_menu", 
    )
    """

# Register your models with the admin
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(TimeTable)  # , TimeTableAdmin)
admin.site.register(LunchMenu)  # , LunchMenuAdmin)
