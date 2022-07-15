from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    middle_name = models.CharField(verbose_name='Отчество', max_length=120, default='')

    def get_full_name(self):
        full_name = super(User, self).get_full_name()
        return full_name + ' ' + self.middle_name
