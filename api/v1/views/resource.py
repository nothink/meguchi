from rest_framework import viewsets  # , permissions

from api.v1.models import Resource
from api.v1.serializers import ResourceSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    """
    vcardリソース用のViewSet
    """

    queryset = Resource.objects.all().order_by("-created")
    serializer_class = ResourceSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        """
        シリアライザの取得
        ここではdataの先頭が配列の時にmany=Trueを指定する
        """
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(ResourceViewSet, self).get_serializer(*args, **kwargs)
