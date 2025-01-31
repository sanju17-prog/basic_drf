from django.urls import path
from .views import StudentApi, OneStudent

urlpatterns = [
    path("student_api/", StudentApi.as_view()),
    path("student_api/<int:pk>/", OneStudent.as_view()),
]
