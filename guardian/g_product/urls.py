from django.urls import path
from g_product import models

from g_product import views

urlpatterns = [
	path('show_product/', views.productListView.as_view(), name='product_list'),
    path('new_product/', views.productCreateView.as_view(), name='product_create'),
    path('<int:pk>', views.productDetailView.as_view(), name='product_detail'),
    path('<int:pk>/delete/', views.productDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/edit/', views.productUpdateView.as_view(), name='product_update'),
]

