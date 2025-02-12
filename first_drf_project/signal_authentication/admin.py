from django.contrib import admin
from .models import StudentSignal


class StudentSignalAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'roll', 'city']

# Register your models here.
admin.site.register(StudentSignal, StudentSignalAdmin)