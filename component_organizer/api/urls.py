from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ContainerViewSet


router = DefaultRouter()
router.register("containers", ContainerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
