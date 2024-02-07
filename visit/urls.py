from .views import add_and_get_visit
from django.urls import path


urlpatterns = [
    path('', add_and_get_visit, name='add-visit'),
]