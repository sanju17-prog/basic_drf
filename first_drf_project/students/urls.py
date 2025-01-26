from django.urls import path
from .views import serialize_single_object, serialize_all_objects, student_api

urlpatterns = [
    path('', serialize_single_object, name='serializing single object'),
    path('serialize_all_objects/', serialize_all_objects, name='serializing all objects'),
    path('student_api/', student_api, name='student_api'),
]
