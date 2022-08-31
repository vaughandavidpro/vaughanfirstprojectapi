from django.urls import path
from . import views

urlpatterns = [
    path('',views.OrderList.as_view()),
    path('list/<int:pk>',views.OrderListDetails.as_view()),
    path('list/update_status/<int:pk>',views.UpdateOrderStatus.as_view()),
    path('list/user_order/<int:pk>',views.GetUserOderById.as_view()),
]
