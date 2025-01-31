from django.urls import path
from .views import StudentAPI, OneStudent

urlpatterns = [
    path("student_api/", StudentAPI.as_view()),
    path("student_retrieve/<int:pk>/", OneStudent.as_view()),
]