# Generated by Django 5.0.3 on 2024-06-21 05:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('logo', models.ImageField(upload_to='media/brand')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='media/product/detail_photo')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_cover', models.ImageField(upload_to='media/product/cover')),
                ('title', models.CharField(max_length=123)),
                ('description', models.TextField()),
                ('size', models.PositiveSmallIntegerField(choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL')])),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('actual_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('brands', models.ManyToManyField(to='product.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.color')),
                ('images', models.ManyToManyField(to='product.image')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'В наличии'), (2, 'Скоро в наличии'), (3, 'Нет в наличии')])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='media/poster')),
                ('description', models.CharField(max_length=223)),
                ('is_first', models.BooleanField()),
                ('is_second', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.storage')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.storage')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.storage')),
            ],
        ),
    ]