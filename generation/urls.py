from django.urls import path, include
from .views import generation_list

urlpatterns = [
    path('', generation_list, name='generation-list'),
]