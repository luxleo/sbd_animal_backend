from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.
def validate_username(username):
    if len(username) > 20 or len(username) < 3:
        raise ValidationError(
            _("%(username) length must in 3 and 20"),
            params={"username": username},
        )


class UserManager(BaseUserManager):
    """
    for create super user method in prompt using username field as email
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Users require an email field")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    first_name = None
    last_name = None

    username = models.CharField(
        max_length=20, unique=True, validators=[validate_username]
    )
    email = models.EmailField(_("your email"), unique=True)
    follower_set = models.ManyToManyField("self", blank=True)
    following_set = models.ManyToManyField("self", blank=True)
    web_site_url = models.URLField(blank=True)
    avatar = models.ImageField(blank=True, upload_to="accounts/%Y/%m/%d")
    height = models.CharField(max_length=6, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    USERNAME_FIELD = "email"  # set email field as username identification
    REQUIRED_FIELDS = []  # required_fields에 default로 email포함되어 있어서 비워줘야 충돌이 없다.
    objects = UserManager()

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return None
