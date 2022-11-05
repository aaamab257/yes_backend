from pyexpat import model
from statistics import mode
from django.db import models
from django.utils import timezone
from material.models import *
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager 
from django.contrib.auth.models import Permission , PermissionsMixin



#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name,is_admin,phone_number , division , state , school ,password=None, password2=None):
      
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          state=state,
          school=school,
          division=division,
          phone_number=phone_number
          
      )
      user.is_superuser=is_admin
      user.is_admin=is_admin
      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email,phone_number ,is_admin, name,division , state , school, password=None):
     
      user = self.create_user(
          email,
          password=password,
          name=name,
          state=state,
          school=school,
          division=division,
          phone_number=phone_number
      )
      user.is_admin = is_admin
      user.save(using=self._db)
      return user

#  Custom User Model
class Student(AbstractBaseUser, PermissionsMixin):
  id = models.AutoField(primary_key=True)
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200)
  is_active = models.BooleanField(default=False)
  division = models.ForeignKey(Division,on_delete=models.CASCADE,null=True)
  state = models.CharField(max_length=255)
  school = models.CharField(max_length=255)
  is_admin = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  phone_number = models.CharField(null=True , unique=True , max_length=15)
  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def __str__(self):
      return str('%s (%s)'% (self.id, self.email))

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin