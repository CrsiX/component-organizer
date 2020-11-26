from django.http.response import Http404
from rest_framework.viewsets import ModelViewSet as _ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from backend.models import ContainerModel as _ContainerModel
from api.serializers import ContainerSerializer as _ContainerSerializer
from api.serializers import SimpleContainerSerializer as _SimpleContainerSerializer


class ContainerViewSet(_ModelViewSet):
    queryset = _ContainerModel.objects.all()
    serializer_class = _ContainerSerializer

    def list(self, request, *args, **kwargs):
        queryset = _ContainerModel.objects.all()
        serializer = _SimpleContainerSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    @action(methods=["GET"], detail=True)
    def path(self, request, pk, **kwargs):
        try:
            ct = _ContainerModel.objects.get(id=pk)
        except _ContainerModel as err:
            raise Http404 from err

        return Response(ct.path)

    @action(methods=["GET"], detail=False)
    def find(self, request, **kwargs):
        cts = _ContainerModel.objects.filter(name__contains=request.GET["name"]).all()

        return Response(list(
            map(
                lambda ct: _ContainerSerializer(ct, context={'request': request}).data,
                cts
            )
        ))
