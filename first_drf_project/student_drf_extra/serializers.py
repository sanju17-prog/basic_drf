from rest_framework import serializers
from .models import StudentDrf

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDrf
        fields = ['id', 'name', 'age', 'roll', 'city']

    def validate_roll(self, roll):
        student = StudentDrf.objects.filter(roll = roll)
        if student.exists():
            raise serializers.ValidationError("Roll no should be unique!!")
        elif roll < 0:
            raise serializers.ValidationError("Roll no should be greater than 0!!")
        elif roll > 200:
            raise serializers.ValidationError("Roll no should be less than 200!!")
        return roll
    
    #object level validation
    def validate(self, attrs):
        nm = attrs.get('name')
        ct = attrs.get('city')
        if nm.lower() == 'rohit' and ct.lower() == 'gandhinagar':
            raise serializers.ValidationError("Rohit can't live in Gandhinagar :/")
        return attrs