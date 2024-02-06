from rest_framework import serializers
from .models import Project

class SimpleProjectSerializer(serializers.ModelSerializer): # 이름, 기수, 년도, 프로필
    class Meta:
        model = Project
        fields = [ 'id', 'title', 'generation_id', 'year', 'project_image' ]

class DetailProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'