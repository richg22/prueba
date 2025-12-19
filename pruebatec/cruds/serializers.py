from rest_framework import serializers
from .models import Usuario, Usuariopending


class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("id", "nombre", "edad", "email")


class UsuariopendingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuariopending
        fields = ("id", "nombre", "edad", "email")
