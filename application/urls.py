from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', AppCreateListView.as_view(), name ='create'),
]
