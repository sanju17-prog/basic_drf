from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSets

router = DefaultRouter()
router.register('students', StudentViewSets, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework_auth1')),
]
