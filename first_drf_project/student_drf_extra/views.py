from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import StudentDrf
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
# Create your views here.

PLEASE_PROVIDE_ID_MSG = 'Please provide the id'
UPDATED_MSG = 'Data updated!!'

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def parse_request_body(self, request):
        if request.body:
            print(f"in views, got request body{request.body}")  
            json_data = request.body.decode('utf-8') # Decodes the raw JSON data (bytes) into a string.
            stream = io.BytesIO(json_data.encode('utf-8')) # Converts the raw JSON data (bytes) into a stream for processing.
            return JSONParser().parse(stream) # Parses the JSON data into a Python dictionary.
        return {}
    
    def get(self, request, *args, **kwargs):
        python_data = self.parse_request_body(request)
        return self.handle_get_request(python_data)

    def post(self, request, *args, **kwargs):
        python_data = self.parse_request_body(request)
        return self.handle_post_request(python_data)

    def patch(self, request, *args, **kwargs):
        python_data = self.parse_request_body(request)
        return self.handle_patch_request(python_data)

    def put(self, request, *args, **kwargs):
        python_data = self.parse_request_body(request)
        return self.handle_put_request(python_data)

    def delete(self, request, *args, **kwargs):
        python_data = self.parse_request_body(request)
        return self.handle_delete_request(python_data)
    
    def handle_get_request(self, python_data):
        student_id = python_data.get('id', None)
        if student_id is not None:
            student = StudentDrf.objects.get(id=student_id)
            serializer = StudentSerializer(student)
            return JsonResponse(serializer.data)
        student = StudentDrf.objects.all()
        serializer = StudentSerializer(student, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def handle_post_request(self, python_data):
        # sourcery skip: class-extract-method
        serializer = StudentSerializer(data=python_data) # Creates a serializer instance with the parsed Python data.
        if serializer.is_valid():
            serializer.save() # Saves the valid data to the database by creating a new Student instance.
            res = {'msg': 'Data created!!'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors, status=400)
    
    def handle_patch_request(self, python_data):
        student_id = python_data.get('id')
        if student_id is not None:
            student = StudentDrf.objects.get(id=student_id)
            serializer = StudentSerializer(student, data=python_data, partial=True)
            if serializer.is_valid():
                res = {'msg': UPDATED_MSG}
                serializer.save()
                return JsonResponse(res)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse({'msg': PLEASE_PROVIDE_ID_MSG}, status=400)
    
    def handle_put_request(self, python_data):
        student_id = python_data.get('id')
        if student_id is not None:
            student = StudentDrf.objects.get(id=student_id)
            serializer = StudentSerializer(student, data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data updated!!'}
                return JsonResponse(res)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse({'msg': PLEASE_PROVIDE_ID_MSG}, status=400)
    
    def handle_delete_request(self, python_data):
        student_id = python_data.get('id')
        if student_id is not None:
            student = StudentDrf.objects.get(id=student_id)
            student.delete()
            res = {'msg': 'Data deleted successfully'}
            return JsonResponse(res)
        return JsonResponse({'msg': PLEASE_PROVIDE_ID_MSG}, status=400)
