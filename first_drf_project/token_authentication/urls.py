from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from rest_framework.authtoken.views import obtain_auth_token

routers = DefaultRouter()
routers.register('studentViewSet', viewset=StudentViewSet, basename='studentViewSet')

urlpatterns = [
    path("", include(routers.urls)),
    path("get_token/", obtain_auth_token, name="obtain_path_token")
]
