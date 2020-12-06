from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from .serializers import UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile


class UserProfileViewSets(viewsets.ModelViewSet):
    """Handle creating and updating of user profile"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
