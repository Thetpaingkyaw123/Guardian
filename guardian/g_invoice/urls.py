from django.urls import path
from g_invoice import models

from g_invoice import views

urlpatterns = [
	path('show_invoice/', views.invoiceListView.as_view(), name='invoice_list'),
    path('new_invoice/', views.invoiceCreateView.as_view(), name='invoice_create'),
    path('<int:pk>', views.invoiceDetailView.as_view(), name='invoice_detail'),
    path('<int:pk>/delete/', views.invoiceDeleteView.as_view(), name='invoice_delete'),
    path('<int:pk>/edit/', views.invoiceUpdateView.as_view(), name='invoice_update'),
]