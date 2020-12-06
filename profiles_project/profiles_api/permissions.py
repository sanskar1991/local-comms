from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    
    def has_object_permission(self, request, view, obj):
        """Checks user is trying to udate his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    
    
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to edit their own profile feed item"""
    
    def has_object_permission(self, request, view, obj):
        """Checks user is trying to udate his own profile feed item"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id