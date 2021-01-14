from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Molimo unesite E-mail adresu.")
        if not username:
            raise ValueError("Molimo unesite korisničko ime.")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


GENDER_CHOICES = (
    (0, 'Muško'),
    (1, 'Žensko'),
    (2, 'Neodređeno')
)

class Account(AbstractBaseUser):
    username            = models.CharField(max_length=30, unique=True)
    email               = models.EmailField(verbose_name="E-mail", max_length=60, unique=True)
    gender              = models.IntegerField(verbose_name="Spol", choices=GENDER_CHOICES, default=2)
    date_of_birth       = models.DateField(verbose_name="Datum rođenja", auto_now=False, auto_now_add=False, default="2001-01-01")
    date_joined         = models.DateTimeField(verbose_name="Date joined", auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name="Last login", auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True