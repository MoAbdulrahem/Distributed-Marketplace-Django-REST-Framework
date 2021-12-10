from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.functional import cached_property
from django.db.models.signals import post_save
from django.dispatch import receiver
from cart.models import Cart
# Create your models here.

# Implementing a custom user model
class UserManager(BaseUserManager):
  
  def create_user(self, username, email, password=None,password2=None):

    if username is None:
      raise ValueError("Username cannot be None")
    if email is None:
      raise ValueError("Email cannot be None")
    
    user = self.model(username=username, email=self.normalize_email(email))
    if password and password2 and password!=password2:
      raise ValueError("Passwords must match.")
    user.set_password(password)

    # if user.username[0]=='m':
    #   print(user.username)
    # user.save(database='db2')
    # else:
    #   user.save(using='default')

    # user.set_password(self.cleaned_data['password'])
    user.save(using=self._db)
    # Cart.objects.create(user=self)
    return user

  def create_superuser(self, username, email, password=None,password2=None):

    user = self.create_user(username, email, password)
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)
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

  @cached_property
  def cart(self):
    cart, created = Cart.objects.get_or_create(user=self)
    return cart

  def get_full_name(self):
      return self.email

  def __str__(self):
      return self.email

@receiver(post_save, sender=User)
def save_user(sender, instance, created, **kwargs):
  if created:
    Cart.objects.create(user=instance)
    # Cart.save()