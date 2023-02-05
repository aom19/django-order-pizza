from django.urls import path
from . import  views

urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('update-status/<int:pk>/', views.OrderStatusUpdateView.as_view(), name='order_status_update'),
    path('user/<int:user_id>/orders/',views.UserOrdersView.as_view(), name ='user_orders'),
    path('user/<int:user_id>/order/<int:order_id>',views.UserOrderDetail.as_view(), name ='user_specific_order')


]