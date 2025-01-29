from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('student_api/', StudentAPI.as_view()),
    path('student_api/<int:pk>/', StudentAPI.as_view())
]
