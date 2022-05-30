from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin

from g_product import models
from g_product import forms
from django.db.models import Q

class productListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.productModel
    context_object_name = 'product_list'
    template_name = 'product_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        sq = self.request.GET.get("search_query")
        search_type = self.request.GET.get("search_type")

        if sq is not None:
            if search_type == "name":
                qs = qs.filter(Q(name__icontains=sq))
            elif search_type == "street":
                qs = qs.filter(Q(street__icontains=sq))

        return qs

class productCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("product_list")
    model = models.productModel
    form_class = forms.productCreateForm
    template_name = 'product_create.html'

class productDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("product_list")
    model = models.productModel
    context_object_name = "product"
    template_name = 'product_delete.html'

class productDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.productModel
    context_object_name = "product"
    template_name = 'product_detail.html'

class productUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("product_list")
    model = models.productModel
    form_class = forms.productUpdateForm
    context_object_name = "product"
    template_name = 'product_update.html'