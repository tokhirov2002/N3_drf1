from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializers


class ProductViews(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
