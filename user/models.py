from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class users(models.Model):
    uname=models.CharField(max_length=10)

    password=models.CharField(max_length=64)

    class Meta:
        db_table='users'

    def __str__(self) -> str:
        return f"{self.id}| Name: {self.uname} | pass: {self.password}\n"