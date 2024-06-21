from rest_framework import status
from rest_framework.views import APIView, Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import UserCreateSerializer, UserListSerializer, ProfileListSerializer, ProfileUpdateSerializer
from .models import MyUser


class UserCreateView(APIView):

    def get(self, request):
        users = MyUser.objects.all()

        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class ProfileListView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_QUERY, description="Имя пользователя", type=openapi.TYPE_STRING,
                              required=True),
            openapi.Parameter('email', openapi.IN_QUERY, description="Email пользователя", type=openapi.TYPE_STRING,
                              required=True),
            openapi.Parameter('phone_number', openapi.IN_QUERY, description="Номер телефона пользователя",
                              type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('address', openapi.IN_QUERY, description="Адрес пользователя", type=openapi.TYPE_STRING),
            openapi.Parameter('cover', openapi.IN_QUERY, description="Обложка пользователя", type=openapi.TYPE_FILE),
            openapi.Parameter('is_stuff', openapi.IN_QUERY, description="Флаг персонала", type=openapi.TYPE_BOOLEAN,
                              default=False),
            openapi.Parameter('is_admin', openapi.IN_QUERY, description="Флаг администратора",
                              type=openapi.TYPE_BOOLEAN, default=False),
            openapi.Parameter('status', openapi.IN_QUERY, description="Статус пользователя", type=openapi.TYPE_INTEGER,
                              enum=[1, 2], default=1),
        ],
        responses={
            200: openapi.Response('200 OK', ProfileListSerializer()),
        }
    )
    def get(self, request):
        user = MyUser.objects.get(id=request.user.id)
        serializer = ProfileListSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type="object",
            properties={
                "username": openapi.Schema(type="string", example='gigi'),
                "email": openapi.Schema(type="string", example='gigi@gigi.com'),
                "phone_number": openapi.Schema(type="string", example='+996990041407'),
                "address": openapi.Schema(type="string", example="Kyrgyzstan"),
                "cover": openapi.Schema(type="string", example='url'),
                "is_stuff": openapi.Schema(type="string", example=1),
                "is_admin": openapi.Schema(type="string", example=1),
                "status": openapi.Schema(type="string", example=1),
            }
        ),
        responses={
            200: openapi.Response('200 OK', ProfileListSerializer()),
        },
    )
    def post(self, request):
        serializer = ProfileUpdateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)