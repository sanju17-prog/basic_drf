from rest_framework import viewsets
from generic_views.serializers import StudentSerializer
from students.models import Student
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    '''
    it will include all the things: 
        create
        update
        partial_update
        delete
        retrieve
    '''

class ReadOnlyStudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer