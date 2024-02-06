from django.shortcuts import render
from .models import Visit
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def add_visit(request):

    visit = Visit()
    visit.save()

    response = {
                "status": "success",
                "message": None,
                "data": None
            }
    
    return Response(response, status=status.HTTP_201_CREATED)


