from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from .auth import CustomAuthToken

routers = DefaultRouter()
routers.register('studentViewSet', viewset=StudentViewSet, basename='studentViewSet')

urlpatterns = [
    path("", include(routers.urls)),
    path("get_token/", CustomAuthToken.as_view())
]