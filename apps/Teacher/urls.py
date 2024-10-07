from django.urls import path
from . import views

app_name = 'Teacher'
urlpatterns = [
    
    path('registration/', views.teacher_list, name='teacher-list'),  
    path('<int:pk>/', views.teacher_detail, name='teacher-detail'),  
    path('classes/<int:pk>/', views.class_detail, name='class-detail') 
]
