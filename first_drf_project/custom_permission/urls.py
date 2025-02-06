from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

routers = DefaultRouter()

routers.register("student_viewset",viewset = StudentViewSet, basename = "student_viewset")

urlpatterns = [
    path("", include(routers.urls)),
    path("auth/", include('rest_framework.urls', namespace='rest_framework_auth'))
]
