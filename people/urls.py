from django.urls import path, include
from .views import people_list

urlpatterns = [
    path('<int:generation_id>', people_list, name='people-list'),
]