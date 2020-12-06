from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from .serializers import UserProfileSerializer, ProfileFeedItemSerializer
from .models import UserProfile, ProfileFeedItem
from .permissions import UpdateOwnProfile, UpdateOwnProfile


class UserProfileViewSets(viewsets.ModelViewSet):
    """Handle creating and updating of user profile"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentiction tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    """Handling profile feed items"""
    serializer_class =  ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (UpdateOwnProfile, IsAuthenticated)
    
    def perform_create(self, serializer):
        """Sets the user profile to logged in user"""
        serializer.save(user_profile=self.request.user)