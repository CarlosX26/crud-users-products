from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from users.permissions import IsSuperUserOrReadOnly
from products.models import Product
from products.serializers import ProductSerializer


class ProductView(ListCreateAPIView, PageNumberPagination):
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ProductViewById(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUserOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "id"
