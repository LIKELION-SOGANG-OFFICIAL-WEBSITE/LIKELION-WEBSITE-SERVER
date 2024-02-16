from rest_framework import serializers
from .models import Application

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class AppDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ['email', 'phone', 'apply_id', 'app5', 'app6', 'isPass']

class IsPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['name', 'student_number', 'field', 'isPass' ]
        