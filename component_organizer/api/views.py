from rest_framework.viewsets import ModelViewSet as _ModelViewSet

from backend.models import ContainerModel as _ContainerModel
from api.serializers import ContainerSerializer as _ContainerSerializer


class ContainerViewSet(_ModelViewSet):
    queryset = _ContainerModel.objects.all()
    serializer_class = _ContainerSerializer
