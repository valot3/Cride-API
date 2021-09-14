"""Users URLs."""

#Django REST Framework
from rest_framework.routers import DefaultRouter 

#Django
from django.urls import path, include

#Project
from cride.users.views import users as users_views



router = DefaultRouter()
router.register(r'users', users_views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
