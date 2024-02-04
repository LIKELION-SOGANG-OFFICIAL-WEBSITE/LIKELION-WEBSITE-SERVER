from django.shortcuts import render
from .models import BabyLion, AdultLion
from .serializers import AdultLionSerializer, BabyLionSerializer
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

@api_view(['GET'])
def people_list(request):
    generation= request.GET.get('code')

    adult_lion_list = AdultLion.objects.filter(generation=generation)
    adult_lion_serializer = AdultLionSerializer(adult_lion_list, many=True)

    baby_lion_list = BabyLion.objects.filter(generation=generation)
    baby_lion_serializer = BabyLionSerializer(baby_lion_list, many=True)

    data = {
        'generation': generation,
        'adult_lion': adult_lion_serializer.data,
        'baby_lion': baby_lion_serializer.data 
    }

    return Response(data, status=status.HTTP_200_OK)
