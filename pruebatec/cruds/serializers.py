from rest_framework import serializers
from .models import Usuario, Usuariopending


class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        # fields = ("id", "nombre", "edad", "email", "password")
        fields = "__all__"


class UsuarioPendingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuariopending
        fields = ("id", "nombre", "edad", "email")
