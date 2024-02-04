from django.urls import path, include
from .views import people_list

urlpatterns = [
    path('generation', people_list, name='people-list'),
]