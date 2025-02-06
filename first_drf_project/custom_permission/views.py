from rest_framework import viewsets
from generic_views.serializers import StudentSerializer
from students.models import Student
from rest_framework.authentication import SessionAuthentication
from .custompermissions import MyPermission
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]
    '''
    it will include all the things: 
        create
        update
        partial_update
        delete
        list
        retrieve
    '''
