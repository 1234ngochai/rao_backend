from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password = None, **extra_fields):
        
        #check if it a valid usernames
        if not username:
            raise ValueError("The username must be set")
        
        # a method from model to normalize username
        username = self.model.normalize_username(username)

        #create an user instace temporally in the memory with all the prefilled parameter
        #should assigned username to username paramenter, as the parameter maybe off ordered
        user = self.model(username = username, **extra_fields)
        
        # hash the user password instead of storing it directly into the database
        user.set_password(password)

        # permanently store the created user into the database
        user.save()

        return user
    
    def create_superuser(self, username, password=None, **extra_fields):
        
        #set default if the value of is staff and superuser not set ensure that 
        # it will create correctly for staff and super user
        # otherwise user the value that it assigned with.

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length = 150, unique = True)

    # Aditional fields
    is_active = models.BooleanField(default= False)

    objects = CustomUserManager()

    # set field to used as unique identifier
    USERNAME_FIELD = 'username'

    # field required for create super user
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username