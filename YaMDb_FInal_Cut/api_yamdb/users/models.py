import random
from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Roles(Enum):
    user = 'Аутентифицированный пользователь'
    moderator = 'Модератор'
    admin = 'Администратор'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


def generation_code():
    return random.randrange(9999)


class UserProfile(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    role = models.CharField(
        choices=Roles.choices(),
        default='user',
        max_length=50,
        verbose_name='Роль'
    )
    bio = models.TextField('О себе', blank=True)
    confirmation_code = models.PositiveIntegerField(
        'Код подтверждения',
        default=generation_code()
    )

    @property
    def is_admin(self):
        return self.role == Roles.admin.name

    @property
    def is_moderator(self):
        return self.role == Roles.moderator.name

# Сколько не пытался, не смог, выходило либо TypeError: encoding without
# a string argument, либо Python int too large to convert to SQLite INTEGER

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
