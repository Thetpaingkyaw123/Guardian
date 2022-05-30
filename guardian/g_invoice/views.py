from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin

from g_invoice import models
from g_invoice import forms
from django.db.models import Q

class invoiceListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.invoiceModel
    context_object_name = 'invoice_list'
    template_name = 'invoice_list.html'

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

class invoiceCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("invoice_list")
    model = models.invoiceModel
    form_class = forms.invoiceCreateForm
    template_name = 'invoice_create.html'

class invoiceDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("invoice_list")
    model = models.invoiceModel
    context_object_name = "invoice"
    template_name = 'invoice_delete.html'

class invoiceDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.invoiceModel
    context_object_name = "invoice"
    template_name = 'invoice_detail.html'

class invoiceUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("invoice_list")
    model = models.invoiceModel
    form_class = forms.invoiceUpdateForm
    context_object_name = "invoice"
    template_name = 'invoice_update.html'