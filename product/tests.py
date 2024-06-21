from django.test import TestCase

# Create your tests here.
# storage_with_greater_old_price = Storage.objects.filter(
#     product__old_price__gt=F('product__actual_price')
# )
# products_with_brand_count = Product.objects.annotate(
#     num_brands=Count('brands')
# )
#
# # Получение объектов Storage, у которых у продукта более двух брендов
# storage_with_multiple_brands = Storage.objects.filter(
#     product__in=products_with_brand_count.filter(num_brands__gt=1)
# )