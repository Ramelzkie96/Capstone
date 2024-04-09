from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
import os

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    is_Faculty = models.BooleanField('Is Faculty', default=False)
    is_Bits = models.BooleanField('Is Bits', default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True) 
    
    def save(self, *args, **kwargs):
        if not self.profile_picture:
            # Set default image path
            default_image_path = 'profile_pics/users.jpg'
            # Check if the default image file exists
            if os.path.exists(default_image_path):
                # Open the default image file and assign it to the profile_picture field
                with open(default_image_path, 'rb') as f:
                    self.profile_picture.save('users.jpg', f, save=False)
        super().save(*args, **kwargs)
    
    objects = CustomUserManager()
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def save(self, *args, **kwargs):
        # Automatically set is_admin and is_staff for superusers
        if self.is_superuser:
            self.is_staff = True

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
