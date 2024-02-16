from rest_framework import serializers
from .models import Application

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class AppDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ['email', 'phone', 'apply_id', 'isAttend', 'app5', 'app6', 'interview11', 'interview12', 'isPass']
        read_only_fields = ['email', 'phone', 'apply_id', 'isAttend', 'app5', 'app6', 'interview11', 'interview12', 'isPass']

class IsPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['name', 'student_number', 'field', 'isPass' ]
        