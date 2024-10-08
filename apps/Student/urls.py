from django.urls import path
from . import views

app_name = 'Student'
urlpatterns = [
    path('list/', views.student_list, name='student_list'),
]
