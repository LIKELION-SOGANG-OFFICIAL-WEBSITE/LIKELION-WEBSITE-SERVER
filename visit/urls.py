from .views import add_visit
from django.urls import path


urlpatterns = [
    path('', add_visit, name='add-visit'),
]