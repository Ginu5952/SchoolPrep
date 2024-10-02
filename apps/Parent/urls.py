from django.urls import path
from . import views


app_name = 'parent-urls'
urlpatterns = [
        path('registration/', views.parent_list, name='parent_list_create'),
        path('verify-email/<str:uidb64>/<str:token>/', views.verify_email, name='verify-email'),
    ]