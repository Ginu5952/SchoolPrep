from django.urls import path
#from apps.Teacher.views.timetable import timetable_view, timetable_update
#from apps.Teacher.views.lunch_menu import lunchmenu_view, lunchmenu_update
from . import views

app_name = "Teacher"
urlpatterns = [
    path("registration/", views.teacher_list, name="teacher-list"),
    path("<int:pk>/", views.teacher_detail, name="teacher-detail"),
    path("classes/<int:pk>/", views.class_detail, name="class-detail"),
    
    path("timetable/view/", views.timetable_view, name="view-timetable"),
    path("timetable/create/", views.timetable_view, name="create-timetable"),
    path("timetable/update/<int:pk>/", views.timetable.timetable_update, name="timetable-update"),

    path("lunchmenu/view/", views.lunchmenu_view, name="view-lunchmenu"),
    path("lunchmenu/create/", views.lunchmenu_view, name="create-lunchmenu"),
    path("lunchmenu/update/<int:pk>/", views.lunchmenu_update, name="update-lunchmenu"),

    path("leave/view/request/", views.leave_request_view, name="leave-request-view"),
    path("leave/update/<int:pk>/", views.update_leave_status, name="update-leave-status"),

    path("message/view/", views.message_view, name="message-view"),
    path("message/write/", views.message_view, name="update-leave-status"),





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