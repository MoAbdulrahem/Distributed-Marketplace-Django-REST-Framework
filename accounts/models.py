from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

# Implementing a custom user model
class UserManager(BaseUserManager):
  
  def create_user(self, username, email, password=None,password2=None):

    if username is None:
      raise ValueError("Username cannot be None")
    if email is None:
      raise ValueError("Email cannot be None")
    
    user = self.model(username=username, email=self.normalize_email(email))
    if password==password2:
      raise ValueError("Passwords must match.")
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, username, email, password=None,password2=None):

    user = self.create_user(username, email, password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return user


class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length = 255, unique=True, db_index=True)
  email = models.EmailField(verbose_name='email address', max_length=255, unique=True, db_index=True)
  password2 = models.CharField(max_length=64)
  is_superuser = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  group = None
  balance = models.PositiveIntegerField(default=0)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['password', 'username', 'password2']

  objects = UserManager() # Telling django how to manage objects of this type "User", by delegating that to the UserManager() class

  def get_full_name(self):
      return self.email

  def __str__(self):
      return self.email
