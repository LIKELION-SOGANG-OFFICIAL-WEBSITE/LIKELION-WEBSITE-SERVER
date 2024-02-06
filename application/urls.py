from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', AppCreateListView.as_view()),
    path('<str:apply_id>',AppDetailView.as_view()),
]
