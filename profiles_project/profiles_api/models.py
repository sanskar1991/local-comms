from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Custom manager to manage UserProfile class"""
    
    def create_user(self, email, name, password=None):
        """create a user by its email"""
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
    def create_superuser(self, email, name, password):
        """create a superuser"""
        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    # first_name = models.CharField(max_length=15)
    # last_name = models.CharField(max_length=15)
    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # full_name = first_name + ' ' + last_name
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def  get_full_name(self):
        """Retrieves full name of a user"""
        return self.name
    
    def get_short_name(self):
        """Retrieves short name of a user"""
        return self.name
    
    def __str__(self):
        """Return string representation of user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Returns instance of ProfilefeedItem model into string"""
        return self.status_content