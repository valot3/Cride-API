"""Circles URLs."""

#Django
from django.urls import path, include

#Django REST Framework
from rest_framework.routers import DefaultRouter

#Project
from cride.circles.views import circles as circle_views
from cride.circles.views import memberships as memberships_views 


router = DefaultRouter()
router.register(r'circles', circle_views.CircleViewSet, basename = 'circle')
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-9_]+)/members',
    memberships_views.MembershipViewSet,
    basename = 'membership'
)

urlpatterns = [
    path('', include(router.urls)),
]

