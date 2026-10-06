from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import PartidaViewSet

router = DefaultRouter()
router.register('partidas', PartidaViewSet, basename='partida')

urlpatterns = [
    # POST {username, password} -> {token}
    path('login/', obtain_auth_token, name='api-login'),
    path('', include(router.urls)),
]
