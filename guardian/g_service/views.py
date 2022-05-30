from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin

from g_service import models
from g_service import forms
from django.db.models import Q

class serviceListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.serviceModel
    context_object_name = 'service_list'
    template_name = 'service_list.html'

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

class serviceCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("service_list")
    model = models.serviceModel
    form_class = forms.serviceCreateForm
    template_name = 'service_create.html'

class serviceDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("service_list")
    model = models.serviceModel
    context_object_name = "service"
    template_name = 'service_delete.html'

class serviceDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.serviceModel
    context_object_name = "service"
    template_name = 'service_detail.html'

class serviceUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("service_list")
    model = models.serviceModel
    form_class = forms.serviceUpdateForm
    context_object_name = "service"
    template_name = 'service_update.html'