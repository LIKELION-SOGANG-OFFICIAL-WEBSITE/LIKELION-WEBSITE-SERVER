from rest_framework import serializers
from .models import Generation

class GenerationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Generation
        fields = '__all__'