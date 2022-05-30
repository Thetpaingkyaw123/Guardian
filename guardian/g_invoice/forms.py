from django import forms
from g_invoice import models
from flatpickr import DatePickerInput
from django.utils import timezone


class invoiceCreateForm(forms.ModelForm):
    class Meta:
        model = models.invoiceModel
        fields = '__all__'
        widgets = {
            'date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }

class invoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = models.invoiceModel
        fields = '__all__'
        widgets = {
            'date': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }
