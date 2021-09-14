"""Circle view."""

#Django REST Framework
from rest_framework import viewsets, mixins

#Serializers
from cride.circles.serializers import CircleModelSerializer

#Project
from cride.circles.models import Circle, Membership

#Permissions
from rest_framework.permissions import IsAuthenticated 
#Custom Permissions
from cride.circles.permissions import IsCircleAdmin

#Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class CircleViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """Circle view set."""

    serializer_class = CircleModelSerializer
    lookup_field = 'slug_name'

    #Filters
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['slug_name', 'name', 'about']
    ordering_fields = ['rides_offered', 'rides_taken', 'name', 'created_at', 'members_limit', 'slug_name']
    ordering = ['-members__count', '-rides_taken', '-rides_offered']
    filter_fields = ['verified', 'is_limited']

    def get_permissions(self):
        """Asign permissions based on the current action.
        
        return: The view returns a list of instances of the permission classes that the view requires. 
        """
        permission_classes = [IsAuthenticated]

        if self.action in ['update', 'partial_update']:
            permission_classes.append(IsCircleAdmin)
        
        return [permission() for permission in permission_classes]


    def get_queryset(self):
        """Restrict list to public-only."""

        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        
        return queryset

    def perform_create(self, serializer):
        """Asign circle admin."""

        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user = user,
            profile = profile,
            circle = circle,
            is_admin = True,
            remaining_invitations = 10
        )

