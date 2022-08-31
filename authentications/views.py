from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from authentications.models import User
from authentications.serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema



class CreateUserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    @swagger_auto_schema(operation_summary='Creating A User')
    def post(self,request):
        create_user_data = request.data
        create_user_data_serializer = self.serializer_class(data = create_user_data)
        if create_user_data_serializer.is_valid():
            create_user_data_serializer.save()
            return Response(data = create_user_data_serializer.data,status=status.HTTP_201_CREATED)
        return Response(data = create_user_data_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

