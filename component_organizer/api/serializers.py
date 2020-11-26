from rest_framework.serializers import HyperlinkedModelSerializer

from backend.models import ContainerModel


class SimpleContainerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ContainerModel
        fields = ["name", "url"]


class ContainerSerializer(HyperlinkedModelSerializer):
    parent = SimpleContainerSerializer()
    children = SimpleContainerSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = ContainerModel
        fields = ["name", "parent", "children"]
