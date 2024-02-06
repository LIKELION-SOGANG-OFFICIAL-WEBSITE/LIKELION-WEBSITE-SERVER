from django.shortcuts import render
from .models import BabyLion, AdultLion
from generation.models import Generation
from .serializers import AdultLionSerializer, BabyLionSerializer
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

@api_view(['GET'])
def people_list(request, generation_id):

    generation = Generation.objects.filter(id=generation_id).values('id', 'number', 'suffix').first()
    
    if generation == None: # 예외 처리: 존재하지 않는 기수일 때(404)
        response = {
            "status": "error",
            "message": "Not found information for the specified generation.",
            "data": None
        }

        return Response(response, status=status.HTTP_404_NOT_FOUND)
    
    adult_lion_list = AdultLion.objects.filter(generation_id=generation_id).order_by('name')
    adult_lion_serializer = AdultLionSerializer(adult_lion_list, many=True)

    baby_lion_list = BabyLion.objects.filter(generation_id=generation_id).order_by('name')
    baby_lion_serializer = BabyLionSerializer(baby_lion_list, many=True)

    if not adult_lion_list: # 예외 처리: 기수에 대한 운영진 리스트가 존재하지 않을 때(404)
        response = {
            "status": "error",
            "message": "No adult lions information exists for the specified generation.",
            "data": None
        }

        return Response(response, status=status.HTTP_404_NOT_FOUND)

    elif not baby_lion_list: # 예외 처리: 기수에 대한 아기 사자 리스트가 존재하지 않을 때(200) = 모집 중
        data = {
        "generation": str(generation['number']) + generation['suffix'],
        "adult_lion": adult_lion_serializer.data,
        "baby_lion": None
        }

        response = {
            "status": "success",
            "message": "No baby lions information exists for the specified generation.",
            "data": data
        }

        return Response(response, status=status.HTTP_200_OK)


    data = {
        "generation": str(generation['number']) + generation['suffix'],
        "adult_lion": adult_lion_serializer.data,
        "baby_lion": baby_lion_serializer.data 
    }

    response = {
        "status": "success",
        "message": None,
        "data": data
    }

    return Response(response, status=status.HTTP_200_OK)
