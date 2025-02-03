from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from generic_views.serializers import StudentSerializer
from rest_framework import viewsets
from students.models import Student

PLEASE_PROVIDE_STUDENT_ID = "Please provide student id"

# Create your views here.
class StudentViewSet(viewsets.ViewSet):
    def print_states(self):
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)

    def list(self, request):
        print("***************************LIST***************************")
        self.print_states()
        student = Student.objects.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk = None):
        print("***************************RETRIEVE***************************")
        self.print_states()
        student_id = pk
        if student_id is not None:
            try:
                student = Student.objects.get(id = student_id)
                serialzer = StudentSerializer(student)
                return Response(serialzer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'msg':str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response({'msg': PLEASE_PROVIDE_STUDENT_ID}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        print("***************************CREATE***************************")
        self.print_states()
        print("I got student data: " + str(request.data))
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response({'msg': serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        print("***************************UPDATE***************************")
        self.print_states()
        student_id = pk
        if student_id is not None:
            try:
                student = Student.objects.get(id = student_id)
                serialzer = StudentSerializer(student, data = request.data)
                if serialzer.is_valid():
                    serialzer.save()
                    return Response({'msg': 'Complete data updated'}, status=status.HTTP_202_ACCEPTED)
                return Response(serialzer.error_messages, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'msg':str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response({'msg': PLEASE_PROVIDE_STUDENT_ID}, status=status.HTTP_404_NOT_FOUND)
    
    def partial_update(self, request, pk = None):
        print("***************************PARTIAL_UPDATE***************************")
        self.print_states()
        student_id = pk
        if student_id is not None:
            try:
                student = Student.objects.get(id = student_id)
                serialzer = StudentSerializer(student, data = request.data, partial = True)
                if serialzer.is_valid():
                    serialzer.save()
                    return Response({'msg': 'Partial data updated'}, status=status.HTTP_202_ACCEPTED)
                return Response(serialzer.error_messages, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'msg':str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response({'msg': PLEASE_PROVIDE_STUDENT_ID}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk = None):
        print("***************************DESTROY***************************")
        self.print_states()
        student_id = pk
        if student_id is not None:
            try:
                student = Student.objects.get(id = student_id)
                if student is not None:
                    student.delete()
                    return Response({'msg': 'Data deleted successfully'}, status=status.HTTP_202_ACCEPTED)
                return Response({'msg':'Invalid student id'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'msg':str(e)}, status=status.HTTP_404_NOT_FOUND)
        return Response({'msg': PLEASE_PROVIDE_STUDENT_ID}, status=status.HTTP_404_NOT_FOUND)