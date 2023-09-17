from rest_framework import serializers
from .models import StudentsModel,TeachersModel
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsModel
        fields = ('name','date_of_birth')

    def create(self, validated_data):
        validated_data['user'] = get_object_or_404(User,username=self.context['request'].user)
        return super(StudentsModel,self).create(validated_data)
    
class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersModel
        fields = ('name','date_of_birth')

    def create(self, validated_data):
        validated_data['user'] = get_object_or_404(User,username=self.context['request'].user)
        return super(TeachersModel,self).create(validated_data)
     