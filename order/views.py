from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from order.models import Order
from order.serializers import OrderSerializer,OrderDetailsSerializer,OrderStatusUpdate,UserOderById
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema

User = get_user_model()

class OrderList(generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary='All Orders')
    def get(self,request):
        all_orders = Order.objects.all()
        all_orders_serializers = self.serializer_class(all_orders,many=True)
        return Response(data = all_orders_serializers.data, status = status.HTTP_202_ACCEPTED)

    @swagger_auto_schema(operation_summary='Creating Orders')
    def post(self,request):
        user = self.request.user
        create_order_data = request.data
        create_order_data_serializer = self.serializer_class(data = create_order_data)
        if create_order_data_serializer.is_valid():
            create_order_data_serializer.save(user_customer = user)
            return Response(data = create_order_data_serializer.data, status=status.HTTP_201_CREATED)
        return Response(data = create_order_data_serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class OrderListDetails(generics.GenericAPIView):

    serializer_class = OrderDetailsSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Details Orders')
    def get(self,request,pk):
        order_details = get_object_or_404(Order,id=pk)
        order_details_serializer = self.serializer_class(instance = order_details)
        return Response(data = order_details_serializer.data, status=status.HTTP_200_OK)
        
    @swagger_auto_schema(operation_summary='Update Orders')
    def put(self,request,pk):
        order_details = get_object_or_404(Order,id=pk)
        update_order_data = self.request.data
        update_order_details = self.serializer_class(data=update_order_data,instance = order_details )
        if update_order_details.is_valid():
            update_order_details.save()
            return Response(data = update_order_details.data, status=status.HTTP_201_CREATED)
        return Response(data = update_order_details.errors,status = status.HTTP_400_BAD_REQUEST)
             
    @swagger_auto_schema(operation_summary='Delete Orders')
    def delete(self,request,pk):
        order_details = get_object_or_404(Order,id=pk)
        order_details.delete()
        return Response(data = {'message' : 'Order deleted successfully'}, status = status.HTTP_204_NO_CONTENT)

 

class UpdateOrderStatus(generics.GenericAPIView):

    serializer_class = OrderStatusUpdate
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_summary='Update Orders Status')
    def put(self,request,pk):
        order_details = get_object_or_404(Order,id=pk)
        update_order_status_data = self.request.data
        update_order_status = self.serializer_class(data = update_order_status_data, instance = order_details)
        if update_order_status.is_valid():
            update_order_status.save()
            return Response(data = update_order_status.data, status=status.HTTP_201_CREATED)
        return Response(data = update_order_status.errors,status = status.HTTP_400_BAD_REQUEST)
             

class GetUserOderById(generics.GenericAPIView):
    serializer_class = UserOderById

    @swagger_auto_schema(operation_summary='Getting A User Orders')
    def get(self,request,pk):
        user = User.objects.get(id = pk)
        user_order = Order.objects.filter(user_customer=user)
        user_serializer = self.serializer_class(instance=user_order,many=True)
        return Response(data=user_serializer.data, status=status.HTTP_200_OK)
