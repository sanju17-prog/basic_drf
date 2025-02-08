from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

routers = DefaultRouter()
routers.register('studentViewSet', viewset=StudentViewSet, basename='studentViewSet')

urlpatterns = [
    path("", include(routers.urls))
]
