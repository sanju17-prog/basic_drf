from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        print(f"request.data: {request.data}")
        return Response({'msg': 'This is post request!!', 'data': request.data})
    return Response({'msg': 'Hello World!!'})

@api_view(['GET', 'POST','PUT', 'PATCH','DELETE'])
def student_api(request):
    if request.method == 'GET':
        student_id = request.data.get('id')
        if student_id is not None:
            student = Student.objects.get(id=student_id)
            student_serializer = StudentSerializer(student)
            return Response(student_serializer.data)
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data)
    
    if request.method == 'POST':
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg': 'Data created!!'})
        return Response(student_serializer.errors)
    
    if request.method == 'PUT':
        student_id = request.data.get('id')
        student = Student.objects.get(id=student_id)
        student_serializer = StudentSerializer(student, data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg': 'Data updated!!'})
        return Response(student_serializer.errors)
    
    if request.method == 'PATCH':
        student_id = request.data.get('id')
        student = Student.objects.get(id=student_id)
        student_serializer = StudentSerializer(student, data=request.data, partial=True)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response({'msg': 'Data updated!!'})
        return Response(student_serializer.errors)
    
    if request.method == 'DELETE':
        student_id = request.data.get('id')
        student = Student.objects.get(id=student_id)
        student.delete()
        return Response({'msg': 'Data deleted!!'})