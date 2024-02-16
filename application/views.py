from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage

from django.template.loader import render_to_string
from django.db.models import Q

from rest_framework import generics, mixins, status
from rest_framework.response import Response

from .models import Application
from .serializers import AppSerializer, AppDetailSerializer, IsPassSerializer
import uuid

class AppCreateListView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = AppSerializer
    
    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        student_number = request.data.get('student_number')
        email = request.data.get('email')
        phone = request.data.get('phone')
        apply_id = uuid.uuid4()

        # 중복 지원자 확인 : (student_number || email )
        # q = Q(name = name) -> name && (student_number || email )
        q = Q()
        q.add (Q(student_number =student_number) | Q(email = email), q.AND )
        exist_app = Application.objects.filter(q) 
        if exist_app.exists(): 
            return Response({'message': 'Duplicate application exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        # context = {'name': name, 'apply_id': apply_id}
        # html_message = render_to_string('email.html', context )
        html_message = render_to_string('email.html', {'name': name, 'apply_id': apply_id})

        # 고유번호를 이메일로 발송
        try:
            subject = '멋쟁이사자처럼 지원서 고유번호 안내 이메일'
            message = f'서강대 멋쟁이사자처럼에 지원하신 걸 환영합니다.\n{name} 님의 지원서 고유번호는 {apply_id} 입니다. \n'
            from_email = 'likelionSG@gmail.com'  # 발신 이메일 주소 입력 -> 발송 시에는 발송 이메일 주소로 발송됨...
            recipient_list = [email]
            #send_mail(subject, '', from_email, recipient_list, html_message=html_message, fail_silently=False)
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except BadHeaderError:
            return Response({'message': 'Invalid email header.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': f'Error sending email: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # 모델 객체 생성 및 저장
        application = Application.objects.create(
            name=name,
            student_number=student_number,
            email=email,
            phone=phone,
            apply_id=apply_id
        )

        serializer = AppSerializer(application)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AppDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = AppDetailSerializer
    lookup_field = 'apply_id' # 고유번호를 이용해서 지원서 조회
    
class IsPassView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = IsPassSerializer
    lookup_field = 'apply_id' # 고유번호를 이용해서 지원서 조회
    

    
    
    
    