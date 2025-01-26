from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# Model object - single student row

PLEASE_PROVIDE_ID_MSG = 'Please provide the id'

def serialize_single_object(request):
    _ = request # to remove unused request warning  
    stu = Student.objects.get(id = 1)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)


def serialize_all_objects(request):
    _ = request
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')


'''
here, we are using @csrf_exempt decorator because we are sending POST request from another server.
and we can use any server to create student data.
'''
@csrf_exempt
def student_api(request):
    json_data = request.body
    stream = io.BytesIO(json_data) # Converts the raw JSON data (bytes) into a stream for processing.
    python_data = JSONParser().parse(stream) # Parses the JSON data into a Python dictionary.

    if request.method == 'GET':
        return handle_get_request(python_data)
    elif request.method == 'POST':
        return handle_post_request(python_data)
    elif request.method == 'PATCH':
        return handle_patch_request(python_data)
    elif request.method == 'PUT':
        return handle_put_request(python_data)
    elif request.method == 'DELETE':
        return handle_delete_request(python_data)
    return JsonResponse({'msg': 'Invalid request'}, status = 400)


def handle_get_request(python_data):
    student_id = python_data.get('id', None)
    if student_id is not None:
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)


def handle_post_request(python_data):
    serializer = StudentSerializer(data=python_data) # Creates a serializer instance with the parsed Python data.
    if serializer.is_valid():
        serializer.save() # Saves the valid data to the database by creating a new Student instance.
        res = {'msg': 'Data created!!'}
        return JsonResponse(res)
    return JsonResponse(serializer.errors, status=400)


def handle_patch_request(python_data):
    student_id = python_data.get('id')
    if student_id is not None:
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data updated!!'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'msg': PLEASE_PROVIDE_ID_MSG}, status=400)


def handle_put_request(python_data):
    student_id = python_data.get('id')
    if student_id is not None:
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student, data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data updated!!'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'msg': PLEASE_PROVIDE_ID_MSG}, status=400)


def handle_delete_request(python_data):
    student_id = python_data.get('id')
    if student_id is not None:
        student = Student.objects.get(id=student_id)
        student.delete()
        res = {'msg': 'Data deleted successfully'}
        return JsonResponse(res)
    return JsonResponse({'msg': PLEASE_PROVIDE_ID_MSG}, status=400)

