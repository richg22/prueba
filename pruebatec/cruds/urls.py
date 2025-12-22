from rest_framework import routers
from .api import UsuarioViewSet, UsuarioPendingViewSet

router = routers.DefaultRouter()

router.register("api/usuarios", UsuarioViewSet, "usuarios")
router.register("api/usuariospending", UsuarioPendingViewSet, "usuariospending")

urlpatterns = router.urls
