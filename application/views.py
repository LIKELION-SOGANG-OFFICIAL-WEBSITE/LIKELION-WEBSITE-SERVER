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
            subject = '멋쟁이사자처럼 지원서 고유번호 안내'
            message = f'서강대 멋쟁이사자처럼에 지원하신 걸 환영합니다.\n {name}님의 지원서 고유번호는 {apply_id} 입니다. \n'
            from_email = 'sogang@likelion.org'  # 발신 이메일 주소 입력
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
        except BadHeaderError:
            return Response({'message': 'Invalid email header.'}, status=status.HTTP_400_BAD_REQUEST)
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
    
    

    
    
    
    