from rest_framework import serializers
from .models import Product, Brand, Category, Storage, Favorite, Poster, Basket


class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('title', 'logo')


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class ProductListSerializer(serializers.ModelSerializer):
    brands = BrandListSerializer(many=True)
    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'main_cover',
            'title',
            'description',
            'brands',
            'category',
            'actual_price',
            'old_price'
        )


class StorageListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = Storage
        fields = ('product',)


class FavoriteCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Favorite
        fields = ('user', 'product')


class ProductPosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'main_cover')


class StoragePosterListSerializer(serializers.ModelSerializer):
    product = ProductPosterSerializer()

    class Meta:
        model = Storage
        fields = ('product',)


class PosterListSerializer(serializers.ModelSerializer):
    product = StoragePosterListSerializer()

    class Meta:
        model = Poster
        fields = '__all__'


class StorageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ('product', 'quantity', 'status')


class BasketListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Basket
        fields = '__all__'


class BasketCreateSerializer(serializers.ModelSerializer):
    #   user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Basket
        fields = '__all__'