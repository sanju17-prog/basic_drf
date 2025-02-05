from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ReadOnlyStudentViewSet

router = DefaultRouter()

router.register("student_viewset", viewset=StudentViewSet, basename="student_viewset")
router.register("read_student_viewset", viewset=ReadOnlyStudentViewSet, basename="read_student_viewset")

urlpatterns = [
    path("", include(router.urls)),
]
