from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # Auth
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.UserCreateView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Not Auth
    path('profile/', views.ProfileListView.as_view())
]

# {
# "username": "bilal",
# "phone_number": "+996770519045",
# "password": "admin"
# }