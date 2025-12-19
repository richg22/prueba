from .models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializers, UsuariopendingSerializers
from nuevapp.tasks import send_async_email


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuariopendingSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = response.data
        status_code = response.status_code

        if status_code == 201:
            email = data.get("email")
            id = data.get("id")
            send_async_email.delay(email, id)

        return response

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
