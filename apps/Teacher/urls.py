from django.urls import path
#from apps.Teacher.views.timetable import timetable_view, timetable_update
from apps.Teacher.views.lunch_menu import lunchmenu_view, lunchmenu_update
from . import views

app_name = "Teacher"
urlpatterns = [
    path("registration/", views.teacher_list, name="teacher-list"),
    path("<int:pk>/", views.teacher_detail, name="teacher-detail"),
    path("classes/<int:pk>/", views.class_detail, name="class-detail"),
    
    path("timetable/view/", views.timetable_view, name="timetable-detail"),
    path("timetable/create/", views.timetable_view, name="timetable-detail"),
    path("timetable/update/<int:pk>/", views.timetable.timetable_update, name="timetable-update"),

    path("lunchmenu/view/", views.lunch_menu.lunchmenu_view, name="lunchmenu-list"),
    path("lunchmenu/create/", views.lunch_menu.lunchmenu_view, name="lunchmenu-list"),
    path("lunchmenu/update/<int:pk>/", views.lunch_menu.lunchmenu_update, name="lunchmenu-detail"),
]
'''
app_name = "Teacher"
urlpatterns = [
    path("registration/", views.teacher_list, name="teacher-list"),
    path("<int:pk>/", views.teacher_detail, name="teacher-detail"),
    path("classes/<int:pk>/", views.class_detail, name="class-detail"),

    # Timetable URLs
    path("timetable/view/", timetable_view, name="timetable-detail"),
    path("timetable/update/<int:pk>/", timetable_update, name="timetable-update"),

    # Lunch Menu URLs
    path("lunchmenu/view/", lunchmenu_list, name="lunchmenu-list"),
    path("lunchmenu/update/<int:pk>/", lunchmenu_update, name="lunchmenu-detail"),
]'''