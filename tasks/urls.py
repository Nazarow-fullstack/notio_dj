from .views import TaskViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path,include
router=DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='command-tasks')

urlpatterns =[
    path('', include(router.urls)),
]