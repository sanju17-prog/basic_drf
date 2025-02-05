from rest_framework import viewsets
from generic_views.serializers import StudentSerializer
from students.models import Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated] #sanjana124 = 17kamlesh14
    '''
    it will include all the things: 
        create
        update
        partial_update
        delete
        list
        retrieve
    '''

class ReadOnlyStudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser] 
    ''' sanjana = sanjana124
    it will include only read-only things: 
        list
        retrieve
    '''