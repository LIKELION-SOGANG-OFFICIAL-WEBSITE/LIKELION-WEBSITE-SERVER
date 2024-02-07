from django.shortcuts import render
from .models import Generation
from .serializers import GenerationSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def generation_list(request):
    generation_list = Generation.objects.all().order_by('number')
    serializer = GenerationSerializers(generation_list, many=True)

    if not generation_list: # 예외 처리: 기수가 존재하지 않을 때
        response = {
            "status": "error",
            "message": "No generations found.",
            "data": None
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    response = {
        "status": "success",
        "message": None,
        "data": serializer.data
    }

    return Response(response, status=status.HTTP_200_OK)