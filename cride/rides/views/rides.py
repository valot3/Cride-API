"""
Rides views.
"""
#Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

#Permissions
from rest_framework.permissions import IsAuthenticated
from cride.circles.permissions.memberships import IsActiveCircleMember

#Serializers
from cride.rides.serializers import (
    CreateRideSerializer,
    RideModelSerializer
)

#Models
from cride.circles.models import Circle

#Utilities
from datetime import timedelta
from django.utils import timezone



class RideViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """
    Rides view set.
    """    

    permission_classes = [IsAuthenticated, IsActiveCircleMember]

    def dispatch(self, request, *args, **kwargs):
        """
        Verify that the circle exists.
        """
        slug_name = kwargs['slug_name']
        self.circle = get_object_or_404(Circle, slug_name=slug_name)
        
        return super(RideViewSet, self).dispatch(request, *args, **kwargs)
    

    def get_serializer_context(self):
        """
        Add circle to serializer context.
        """
        context = super(RideViewSet, self).get_serializer_context()
        context['circle'] = self.circle
        
        return context

    
    def get_serializer_class(self):
        """
        Return serializer based on action.
        """
        if self.action == 'create':
            return CreateRideSerializer

        return RideModelSerializer

    
    def get_queryset(self):
        """
        Return active circle's rides.
        """
        offset = timezone.now() + timedelta(minutes=10)

        return self.circle.ride_set.filter(
            departure_date__gte = offset,
            is_active = True,
            available_seats__gte = 1
        )