from django.shortcuts import render
from students.models import Student
from generic_views.serializers import StudentSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

class StudentApi(ListAPIView, ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class OneStudent(RetrieveAPIView, UpdateAPIView, DestroyAPIView, 
                 RetrieveDestroyAPIView, RetrieveUpdateAPIView, 
                 RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer