from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import HyperlinkedRelatedField

from backend.models import ContainerModel


class ContainerSerializer(HyperlinkedModelSerializer):
    children = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="containermodel-detail"
    )

    class Meta:
        model = ContainerModel
        fields = ["name", "parent", "children"]
