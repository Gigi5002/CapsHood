from django.db.models import F
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, APIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .serializers import (
    StorageListSerializer,
    PosterListSerializer,
    BrandListSerializer,
    StorageCreateSerializer,
    BasketListSerializer, BasketCreateSerializer
)
from .models import (
    Brand,
    Storage,
    Poster,
    Basket,
)
from .filters import StorageFilter
from .paginations import StoragePagination


class IndexView(APIView):

    def get(self, request):
        # Requests
        posters = Poster.objects.all()

        brands = Brand.objects.all()

        bestseller = Storage.objects.all()

        product_action = Storage.objects.filter(product__old_price__gt=F('product__actual_price'))

        # Serializers
        posters_serializer = PosterListSerializer(posters, many=True)
        brands_serializer = BrandListSerializer(brands, many=True)
        bestseller_serializer = StorageListSerializer(bestseller, many=True)
        product_action_serializer = StorageListSerializer(product_action, many=True)

        data = {
            'posters': posters_serializer.data,
            'brands': brands_serializer.data,
            'bestseller': bestseller_serializer.data,
            'product_action': product_action_serializer.data,
        }

        return Response(data)


class ProductListView(ListCreateAPIView):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    queryset = Storage.objects.all()
    serializer_class = StorageListSerializer
    search_fields = ['product__title']
    ordering_fields = ['product__actual_price']
    filterset_class = StorageFilter
    pagination_class = StoragePagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StorageListSerializer
        elif self.request.method == 'POST':
            return StorageCreateSerializer


class ProductDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Storage.objects.all()
    serializer_class = StorageListSerializer


class StorageCreateView(CreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateSerializer


class StorageUpdateView(UpdateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateSerializer


class StorageDeleteView(DestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateSerializer


class BasketAddAPIView(CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketListSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        product = instance.storage.product
        storage = Storage.objects.filter(product=product).first()
        if not storage or storage.quantity <= 0 or storage.status != 1:
            raise ValidationError("Данный продукт недоступен для добавления в корзину.")

        storage.quantity -= instance.quantity
        storage.save()

    # def get_queryset(self):
    #     return BasketAddAPIView.objects.filter(user=self.request.user.id)


class BasketListAPIView(ListCreateAPIView):
    serializer_class = BasketListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)


class BasketUpdateRemoveAPIView(RetrieveUpdateDestroyAPIView):
    # queryset = Basket.objects.all()
    serializer_class = BasketCreateSerializer

    def perform_destroy(self, instance):
        product = instance.storage.product
        storage = Storage.objects.get(product=product)
        storage.quantity += instance.quantity
        storage.save()

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)

# Сериализаторы без дженериков:

# class ProductListView(APIView):
#
#     def get(self, request):
#
#         products = Storage.objects.all()
#
#         serializer = StorageListSerializer(products, many=True)
#
#         return Response(serializer.data)
#
#     def post(self, request):
#
#         serializer = FavoriteCreateSerializer(data=request.data, context={'request': request})
#
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)
#         return Response(status.HTTP_400_BAD_REQUEST)