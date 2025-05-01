from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('books/<int:book_id>/reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
]
