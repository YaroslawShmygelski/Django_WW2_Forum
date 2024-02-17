from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    photo = models.ImageField(upload_to='photos/pofile/%Y/%m/%d/', null=True)
    region=models.CharField(null=True, max_length=50)