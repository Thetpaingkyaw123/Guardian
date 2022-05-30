from django.db import models

# Create your models here.
from django.utils import timezone
from flatpickr import DatePickerInput


class invoiceModel(models.Model):
    name = models.CharField(max_length=20,)
    invoiceno = models.CharField(max_length=30,)
    date = models.DateField(verbose_name='date', default=timezone.now())
    customerph = models.CharField(max_length=30,)
    itemdescription = models.CharField(max_length=30,)
    quantity = models.CharField(max_length=20,)
    prices = models.CharField(max_length=50,)
    amount = models.CharField(max_length=50,)
    discount = models.CharField(max_length=50,)
    total = models.CharField(max_length=500,)





