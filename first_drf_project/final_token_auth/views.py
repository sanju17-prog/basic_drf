from signal_authentication.models import StudentSignal
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from token_authentication.serializers import StudentSerializer
# Create your views here.

class StudentViewSet(ModelViewSet):
    # print("reached here")
    queryset = StudentSignal.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
