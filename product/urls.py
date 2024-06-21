from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.ProductListView.as_view()),
    path('index/', views.IndexView.as_view()),
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view()),
    path('storage_create/', views.StorageCreateView.as_view()),
    path('storage_update/<int:pk>/', views.StorageUpdateView.as_view()),
    path('storage_delete/<int:pk>/', views.StorageDeleteView.as_view()),
    path('basket/add/', views.BasketAddAPIView.as_view(), name='basket-add'),
    path('basket/update_remove/<int:pk>/', views.BasketUpdateRemoveAPIView.as_view()),
    path('basket/list/', views.BasketListAPIView.as_view()),
]