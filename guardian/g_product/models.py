from django.db import models

# Create your models here.
from django.utils import timezone
from flatpickr import DatePickerInput


class productModel(models.Model):
    name = models.CharField(max_length=20,)
    model = models.CharField(max_length=300,)
    serialnumber = models.CharField(max_length=30,)
    quantity = models.CharField(max_length=20,)
    invertorydate = models.DateField(verbose_name='invertorydate', default=timezone.now())
    warrantydate = models.DateField(verbose_name='warrantydate', default=timezone.now())
    expireddate = models.DateField(verbose_name='expireddate', default=timezone.now())
    amount = models.CharField(max_length=20,)
    remark = models.CharField(max_length=500,)
