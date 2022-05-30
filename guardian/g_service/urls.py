from django.urls import path
from g_service import models

from g_service import views

urlpatterns = [
	path('show_service/', views.serviceListView.as_view(), name='service_list'),
    path('new_service/', views.serviceCreateView.as_view(), name='service_create'),
    path('<int:pk>', views.serviceDetailView.as_view(), name='service_detail'),
    path('<int:pk>/delete/', views.serviceDeleteView.as_view(), name='service_delete'),
    path('<int:pk>/edit/', views.serviceUpdateView.as_view(), name='service_update'),
]