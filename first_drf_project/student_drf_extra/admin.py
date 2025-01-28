from django.contrib import admin
from .models import StudentDrf
# Register your models here.
@admin.register(StudentDrf)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','roll','city']