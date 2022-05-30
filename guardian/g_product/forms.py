from django import forms
from g_product import models
from flatpickr import DatePickerInput
from django.utils import timezone


class productCreateForm(forms.ModelForm):
    class Meta:
        model = models.productModel
        fields = '__all__'
        widgets = {
            'invertorydate': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'warrantydate': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'expireddate': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }

class productUpdateForm(forms.ModelForm):
    class Meta:
        model = models.productModel
        fields = '__all__'
        widgets = {
            'invertorydate': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'warrantydate': DatePickerInput(options = { "dateFormat": "d.m.y",}),
            'expireddate': DatePickerInput(options = { "dateFormat": "d.m.y",}),
        }
