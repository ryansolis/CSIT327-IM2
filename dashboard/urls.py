from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('customer', views.DashboardCustomerView.as_view(), name="customer_view"),
    path('product', views.DashboardProductView.as_view(), name="product_view"),
    path('product/register', views.ProductRegistrationView.as_view(), name="register_view")
]
