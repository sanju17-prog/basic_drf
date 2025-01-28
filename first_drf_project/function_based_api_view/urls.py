from .views import hello_world, student_api
from django.urls import path

urlpatterns = [
    path('hello/', hello_world, name='hello'),
    path('student_api/', student_api, name='student_api'),
]
