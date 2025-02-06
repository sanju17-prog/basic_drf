from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST','PUT', 'PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, pk = None):
    if request.method == 'GET':
        student_id = request.data.get('id')
        if student_id is not None:
            student = Student.objects.get(id=student_id)
            student_serializer = StudentSerializer(student)
            return Response(student_serializer.data, status= status.HTTP_200_OK)
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg': 'Data created!!'}, status=status.HTTP_201_CREATED)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        student_id = request.data.get('id')
        student = Student.objects.get(id=student_id)
        student_serializer = StudentSerializer(student, data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg': 'Data updated!!'}, status=status.HTTP_201_CREATED)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        student_id = request.data.get('id')
        student = Student.objects.get(id=student_id)
        student_serializer = StudentSerializer(student, data=request.data, partial=True)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg': 'Data updated!!'}, status=status.HTTP_201_CREATED)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        student_id = request.data.get('id')
        student = Student.objects.get(id=student_id)
        student.delete()
        return Response({'msg': 'Data deleted!!'},status=status.HTTP_202_ACCEPTED)