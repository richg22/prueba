from .models import Usuario, Usuariopending
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UsuarioSerializers, UsuarioPendingSerializers
from nuevapp.tasks import send_async_email, send_winner_email
from rest_framework.permissions import IsAuthenticated


class UsuarioViewSet(viewsets.ModelViewSet):

    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializers
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=["get"])
    def random(self, request, *args, **kwargs):
        usuario = self.get_queryset().order_by("?").first()
        serializer = self.get_serializer(usuario)
        send_winner_email.delay(usuario.email)

        print(serializer)
        return Response(serializer.data)


class UsuarioPendingViewSet(viewsets.ModelViewSet):
    queryset = Usuariopending.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioPendingSerializers

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = response.data
        status_code = response.status_code
        print("NO FUNCIONA DASHDJKAS")

        if status_code == 201:
            email = data.get("email")
            id = data.get("id")
            send_async_email.delay(email, id)

        return response

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
