from multiprocessing.sharedctypes import Value
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, fullname, username, email, password=None):
        if not email:
            raise ValueError('empty email')
        if not username:
            raise ValueError('empty username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            fullname=fullname,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, fullname, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            fullname=fullname,
            password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    RETAURANT = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (RETAURANT, 'Retaurant'),
        (CUSTOMER, 'Customer')
    )
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICE, default=2)
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'fullname']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
