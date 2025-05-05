from rest_framework import mixins, viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer