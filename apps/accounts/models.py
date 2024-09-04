from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a user with an email and password"""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)


class Customer(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Admin rights (access to the admin interface)
    is_superuser = models.BooleanField(default=False)  # Full rights, including creating superusers
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'  # Email will be the unique identifier
    REQUIRED_FIELDS = ['first_name', 'last_name']  # These fields are needed for creating a user via shell

    objects = CustomerManager()

    class Meta:
        db_table = "account"
    
    def __str__(self):
        """Return the string representation of the customer"""
        return self.email

    def get_full_name(self):
        """Return the full name of the customer"""
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """Return the short name (first name) of the customer"""
        return self.first_name

    def has_perm(self, perm, obj=None):
        """Return whether the customer has a specific permission"""
        return self.is_superuser or super().has_perm(perm, obj)

    def has_module_perms(self, app_label):
        """Return whether the customer has permission to view the app"""
        return self.is_superuser or super().has_module_perms(app_label)
