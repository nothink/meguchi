from rest_framework import serializers

from api.v1.models import Resource


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    """
    vcardリソース用のモデルシリアライザ
    """

    class Meta:
        model = Resource
        fields = ["key", "url", "fetched", "created"]
