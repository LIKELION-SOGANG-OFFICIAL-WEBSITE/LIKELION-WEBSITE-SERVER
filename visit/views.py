from django.shortcuts import render
from .models import Visit
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

@api_view(['POST', 'GET'])
def add_and_get_visit(request):

    if request.method == 'POST':
        visit = Visit()
        visit.save()

        response = {
                    "status": "success",
                    "message": None,
                    "data": None
                }
        
        return Response(response, status=status.HTTP_201_CREATED)
    
    elif request.method == 'GET':
        now = datetime.now()
        today = now.date()

        total_visit = Visit.objects.count()
        today_visit = Visit.objects.filter(date=today).count()

        data = {
            "total_visit" : total_visit,
            "today_visit" : today_visit
        }

        response = {
                    "status": "success",
                    "message": None,
                    "data": data
                }

        return Response(response, status=status.HTTP_200_OK)


