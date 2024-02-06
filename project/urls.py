from .views import ProjectViewset
from django.urls import path, include


urlpatterns = [
    path('<int:generation_id>/', ProjectViewset.as_view({'get': 'list'}), name='project-list'),
]