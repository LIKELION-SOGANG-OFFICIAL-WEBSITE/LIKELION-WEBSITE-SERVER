from rest_framework import serializers
from .models import BabyLion, AdultLion

class BabyLionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BabyLion
        fields = '__all__'

class AdultLionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdultLion
        fields = '__all__'