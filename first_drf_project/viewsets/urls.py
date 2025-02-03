from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

# router object
router = DefaultRouter()

# registering StudentViewSet with router
router.register('studentViewSet', viewset=StudentViewSet, basename="studentViewSet")

urlpatterns = [
    path("", include(router.urls)),
]
