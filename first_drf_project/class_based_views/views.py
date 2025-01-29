from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from students.models import Student
from .serializers import StudentSerializer

# Create your views here.
INVALID_STUDENT_ID_MSG = 'Invalid student id'

class StudentAPI(APIView):
    def get(self, request, format = None, pk = None):
        student_id = pk
        if student_id is not None:
            try:
                student = Student.objects.get(id = student_id)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format = None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format = None, pk = None):
        student_id = pk
        if student_id is not None:
            student = Student.objects.get(id = student_id)
            serializer = StudentSerializer(student, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Complete data update successful!!'}, status=status.HTTP_202_ACCEPTED)
            return Response({'msg': 'make sure all the required fields are provided'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg':INVALID_STUDENT_ID_MSG}, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, format = None, pk = None):
        student_id = pk
        if student_id is not None:
            student = Student.objects.get(id = student_id)
            serializer = StudentSerializer(student, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Partial data updated!!'},status=status.HTTP_202_ACCEPTED)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg':INVALID_STUDENT_ID_MSG}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format = None, pk = None):
        student_id = pk
        if student_id is not None:
            student = Student.objects.get(id = student_id)
            student.delete()
            return Response({'msg':'Student deleted successfully!!'}, status=status.HTTP_202_ACCEPTED)
        return Response({'msg':INVALID_STUDENT_ID_MSG}, status=status.HTTP_400_BAD_REQUEST)
