from django.shortcuts import render
from  django.core.mail import send_mail, BadHeaderError
from rest_framework import generics, mixins, status
from rest_framework.response import Response

from .models import Application
from .serializers import AppSerializer
import uuid

class AppCreateListView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = AppSerializer
    
    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        student_number = request.data.get('student_number')
        email = request.data.get('email')
        field = request.data.get('field')
        apply_id = uuid.uuid4()
        
        try:
            subject = '지원서 고유번호 안내 메일'
            message = f'{name}님의 지원서 고유번호는 {apply_id} 입니다'
            from_email = 'sogang@likelion.org'  # 발신 이메일 주소 입력
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
        except BadHeaderError:
            return Response({'message': 'Invalid email header. Please try again.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # 예외가 발생하면 사용자에게 적절한 오류 메시지 반환
            return Response({'message': f'Error sending email: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # 모델 객체 생성 및 저장
        application = Application.objects.create(
            name=name,
            student_number=student_number,
            email=email,
            field=field,
            apply_id=apply_id
        )

        serializer = AppSerializer(application)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AppDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = AppSerializer
    lookup_field = 'apply_id'
    
    def get(self, request, *args, **kwargs):
        apply_id = self.kwargs.get('apply_id')
        
        if not apply_id:
            return Response({'message': 'Invalid ID or name'}, status=status.HTTP_404_NOT_FOUND)
        try:
            app = Application.objects.get(apply_id=apply_id)
        except Application.DoesNotExist:
            return Response({'message': 'Invalid ID or name'}, status=status.HTTP_404_NOT_FOUND)
        serializer =   AppSerializer(app)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        apply_id = self.kwargs.get('apply_id')
        
        if not apply_id:
            return Response({'message': 'Invalid ID or name'}, status=status.HTTP_404_NOT_FOUND)
        try:
            app = Application.objects.get(apply_id=apply_id)
        except Application.DoesNotExist:
            return Response({'message': 'Invalid ID or name'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AppSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    

    
    
    
    