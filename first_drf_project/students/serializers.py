from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    roll = serializers.IntegerField()
    city = serializers.CharField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data): 
        '''
        here, instance is the object which is already there stored in DB, and we want to update 
        and validated_data is the data which we want to update.
        '''
        instance.name = validated_data.get('name', instance.name)
        '''
        here, instance.name is the name which is already there in the instance object and
        validated_data.get('name', instance.name) is the name which we want to update.
        so 'name' it will fetch and if it gets the name then it will update the name 
        otherwise it will keep the same name using instance.name.
        '''
        instance.age = validated_data.get('age', instance.age)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance