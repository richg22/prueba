from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):
    edad = models.IntegerField(default=0)
    email = models.EmailField(max_length=100, unique=True, default="")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = "cruds_usuario"


class Usuariopending(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, default="")
    edad = models.IntegerField(default=0)
    email = models.CharField(max_length=100, default="")
    token = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "cruds_usuariopending"
