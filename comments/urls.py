from django.contrib import admin
from django.urls import path, include
from .views import CommentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register(r'comments', CommentViewSet, basename='task')

urlpatterns =[
    path('', include(router.urls)),
]

