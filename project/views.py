from django.shortcuts import render
from .models import Project
from .serializers import SimpleProjectSerializer, DetailProjectSerializer
from rest_framework.viewsets import ModelViewSet
from generation.models import Generation
from rest_framework.response import Response
from rest_framework import status

class ProjectViewset(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = DetailProjectSerializer

    def list(self, request, *args, **kwargs):
        generation_id = self.kwargs.get('generation_id', None)

        if generation_id:
            generation = Generation.objects.filter(id=generation_id).first()

            if generation == None: # 예외처리: 존재하지 않는 기수 ID일 때 (404)
                response = {
                    "status": "error",
                    "message": "Not found information for the specified generation.",
                    "data": None
                }
                return Response(response, status=status.HTTP_404_NOT_FOUND)
            
            queryset = self.queryset.filter(generation_id=generation_id)
            serializer = self.get_serializer(queryset, many=True)
            
            if not queryset: # 예외 처리: 해당 기수에 대한 프로젝트가 존재하지 않을 때 (200)

                response = {
                    "status": "success",
                    "message": "No projects information exists for the specified generation.",
                    "data": None
                }

                return Response(response, status=status.HTTP_200_OK)
                

            data = {
                "generation": str(generation.number) + generation.suffix,
                "project_list": serializer.data
            }

            response = {
                "status": "success",
                "message": None,
                "data": data
            }

            return Response(response, status=status.HTTP_200_OK)
