from django_filters import rest_framework as filters
from .models import Storage


class StorageFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="product__actual_price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="product__actual_price", lookup_expr='lte')

    class Meta:
        model = Storage
        fields = ('status', 'product__actual_price')