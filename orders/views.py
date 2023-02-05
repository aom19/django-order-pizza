from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from . import serializers
from .models import Order
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
# Create your views here.

User = get_user_model()

class OrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data ={'message': 'Hello, Order!' }, status = status.HTTP_200_OK)



class OrderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]



    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders , many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data
        user = request.user
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class OrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        data = request.data
        serializer = self.serializer_class(instance=order, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class OrderStatusUpdateView(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusUpadateSerializer
    permission_classes = [IsAdminUser]
    def put(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        data = request.data
        serializer = self.serializer_class(instance=order, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserOrdersView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    permission_classes = [IsAuthenticated]


    def get(self, request,user_id):
        user = User.objects.get(pk=user_id)

        orders = Order.objects.filter(customer=user)
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserOrderDetail(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id, order_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer=user).get(pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

