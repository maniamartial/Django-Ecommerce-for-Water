from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.


class PhoneNumbers(models.Model):
    name = models.ForeignKey(User, on_delete=CASCADE, blank=True, null=True)
    phone = models.IntegerField()

    def __str__(self):
        return f'{self.id}'
