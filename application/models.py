from django.db import models
import uuid

class Application(models.Model):
    APPLY_FIELD = (
        ('FRONTEND', 'Front'),
        ('BACKEND', 'Back'),
    )
    # 지원자 정보
    name = models.CharField(max_length=20)
    student_number=models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    

    apply_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    # 지원서 항목
    field = models.CharField(max_length=20, choices = APPLY_FIELD, null=True, blank=True)
    app1 = models.TextField(null=True, blank=True)
    app2 = models.TextField(null=True, blank=True)
    app3 = models.TextField(null=True, blank=True)
    app4 = models.TextField(null=True, blank=True)
    app5 = models.TextField(null=True, blank=True)
    app6 = models.TextField(null=True, blank=True)
    isAttend = models.BooleanField(default = True) # 교육세션 참여 여부

    # 면접 참석 가능 날짜
    interview1 = models.BooleanField(default = False) 
    interview2 = models.BooleanField(default = False) 
    interview3 = models.BooleanField(default = False) 
    interview4 = models.BooleanField(default = False) 
    interview5 = models.BooleanField(default = False) 
    interview6 = models.BooleanField(default = False) 
    interview7 = models.BooleanField(default = False) 
    interview8 = models.BooleanField(default = False) 
    interview9 = models.BooleanField(default = False) 
    interview10 = models.BooleanField(default = False) 
    interview11 = models.BooleanField(default = False) 
    interview12 = models.BooleanField(default = False) 

    github = models.CharField(max_length=100, null=True, blank=True)

    #합격 여부
    isPass = models.BooleanField(default = False)
    
    def __str__(self):
        return "{} 개발 {} 의 지원서".format(self.field, self.name)
    
    
    