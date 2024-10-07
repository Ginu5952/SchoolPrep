from django.urls import path
from . import views


app_name = 'parent-urls'
urlpatterns = [
        path('registration/', views.parent_list, name='parent_list_create'),
        path('verify-email/<str:uidb64>/<str:token>/', views.verify_email, name='verify_email'),
        path('view/profile/children/', views.student_info, name='children_profile_view'),
        path('view/profile/', views.parent_info, name='parent_profile_view'),
        path('edit/profile/',views.edit_profile, name='edit_view')
    ]