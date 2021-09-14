"""Users views."""

#Django REST Framework 
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action

#Serializers
from cride.circles.serializers import CircleModelSerializer
from cride.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSingUpSerializer,
    AccountVerificationSerializer,
)
from cride.users.serializers.profiles import ProfileModelSerializer

#Project
from cride.users.models import User
from cride.circles.models import Circle

#Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from cride.users.permissions import IsAccountOwner



class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):
    """Users view set.
    
    Handle users login, singup and account verification.
    """

    queryset = User.objects.filter(is_active=True, is_client=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'


    def get_permissions(self):
        """Assign permissions based on action."""

        if self.action in ['login', 'singup', 'account_verification']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', 'profile']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]

        return [permission() for permission in permissions]

 
    @action(detail=False, methods=['POST'])
    def login(self, request):
        """Users sing in."""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }

        return Response(data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['POST'])
    def singup(self, request):
        """Users sing up."""

        serializer = UserSingUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['POST'])
    def account_verification(self, request):
        """Verify the users account."""

        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulations, now go share some rides!'}

        return Response(data, status=status.HTTP_200_OK)
    

    @action(detail=True, methods=['PUT', 'PATCH'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""

        user = self.get_object()
        profile = user.profile
        is_partial = request.method == 'PATCH' #Bool
        serializer = ProfileModelSerializer(
            profile,
            data = request.data,
            partial = is_partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data

        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response."""

        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        circles = Circle.objects.filter(
            members = request.user,
            membership__is_active = True
        )
        data = {
            'user': response.data,
            'circles': CircleModelSerializer(circles, many=True).data
        }

        response.data = data

        return response
