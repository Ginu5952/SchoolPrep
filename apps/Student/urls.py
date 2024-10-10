from django.urls import path
from . import views

app_name = 'Student'
urlpatterns = [
    path('list/', views.student_list, name='student_list'),
    path('view/lunchmenu/', views.lunchmenu_view, name='view-lunchmenu'),
]
