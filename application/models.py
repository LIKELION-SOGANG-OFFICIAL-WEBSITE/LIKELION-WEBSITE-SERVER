from django.db import models
import uuid

class Application(models.Model):
    APPLY_FIELD = (
        ('FRONTEND', 'Front'),
        ('BACEKEND', 'Back'),
    )
    # 지원자 정보
    name = models.CharField(max_length=20)
    student_number=models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    field = models.CharField(max_length=20, choices = APPLY_FIELD)
    
    apply_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    # 지원서 항목
    app1 = models.TextField(null=True, blank=True)
    app2 = models.TextField(null=True, blank=True)
    app3 = models.TextField(null=True, blank=True)
    app4 = models.TextField(null=True, blank=True)
    app5 = models.TextField(null=True, blank=True)
    app6 = models.TextField(null=True, blank=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return "{} 개발 {} 의 지원서".format(self.field, self.name)
    
    
    