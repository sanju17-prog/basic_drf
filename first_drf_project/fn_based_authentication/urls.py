from django.urls import path
from .views import student_api

urlpatterns = [
    path('student_api/', student_api, name = 'student_api'),
    path('student_api/<int:pk>', student_api, name = 'student_api'),
]
