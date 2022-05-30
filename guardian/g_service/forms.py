from django import forms
from g_service import models
from flatpickr import DatePickerInput
from django.utils import timezone


class serviceCreateForm(forms.ModelForm):
    class Meta:
        model = models.serviceModel
        fields = '__all__'
        widgets = {
            'servicingdate': DatePickerInput(options = { "dateFormat": "d.m.y",}),

        }

class serviceUpdateForm(forms.ModelForm):
    class Meta:
        model = models.serviceModel
        fields = '__all__'
        widgets = {
            'servicingdate': DatePickerInput(options = { "dateFormat": "d.m.y",}),

        }
