from django.urls import path
from . import views


app_name = 'parent-urls'
urlpatterns = [
        path('registration/', views.parent_list, name='parent_list_create'),
        path('verify-email/<str:uidb64>/<str:token>/', views.verify_email, name='verify_email'),
        path('view/profile/children/', views.student_info, name='children_profile_view'),
        path('view/profile/', views.parent_info, name='parent_profile_view'),
        path('edit/profile/',views.edit_profile, name='edit_view'),
        path('apply/leave/',views.parent_leave_list_create, name='apply_leave'),
        path('write/message/', views.write_message, name='write-message'),
        path('view/timetable/', views.timetable_view, name='view-timetable'),
        path('view/lunchmenu/', views.lunchmenu_view, name='view-lunch-menu')

    ]