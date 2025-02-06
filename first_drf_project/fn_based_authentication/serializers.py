from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_roll(self, roll):
        student = Student.objects.filter(roll = roll)
        if student.exists():
            raise serializers.ValidationError("Roll no should be unique!!")
        elif roll < 0:
            raise serializers.ValidationError("Roll no should be greater than 0!!")
        elif roll > 200:
            raise serializers.ValidationError("Roll no should be less than 200!!")
        return roll