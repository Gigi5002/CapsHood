from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError

User = get_user_model()


class Brand(models.Model):
    title = models.CharField(max_length=123)
    logo = models.ImageField(upload_to='media/brand')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.ImageField(upload_to='media/product/detail_photo')


class Product(models.Model):
    main_cover = models.ImageField(
        upload_to='media/product/cover'
    )
    title = models.CharField(
        max_length=123
    )
    description = models.TextField()
    brands = models.ManyToManyField(Brand)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )
    size = models.PositiveSmallIntegerField(
        choices=(
            (1, 'XS'),
            (2, 'S'),
            (3, 'M'),
            (4, 'L'),
            (5, 'XL'),
            (6, 'XXL')
        )
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT
    )
    old_price = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=0.00,
        blank=True,
        null=True
    )
    actual_price = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=0.00
    )
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.title

    def clean(self):
        old_price = self.old_price
        if old_price > 0.00:
            if old_price <= self.actual_price:
                raise ValidationError({'old_price': 'Старая цена должна быть больше!'})
        return super(Product, self).clean()


class Storage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )
    quantity = models.PositiveSmallIntegerField(default=0)
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'В наличии'),
            (2, 'Скоро в наличии'),
            (3, 'Нет в наличии'),
        )
    )

    def __str__(self):
        return str(self.product)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Storage, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} --> {self.product}"


class Poster(models.Model):
    product = models.ForeignKey(Storage, on_delete=models.PROTECT)
    logo = models.ImageField(upload_to='media/poster')
    description = models.CharField(max_length=223)
    is_first = models.BooleanField()
    is_second = models.BooleanField()

    def __str__(self):
        return str(self.product)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    storage = models.ForeignKey('Storage', on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=0)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.storage.product.title} ({self.quantity})"