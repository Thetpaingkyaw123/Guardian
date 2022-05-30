from django.db import models

# Create your models here.
from django.utils import timezone
from flatpickr import DatePickerInput


class serviceModel(models.Model):
    name = models.CharField(max_length=20,)
    address = models.CharField(max_length=300,)
    phonenumber = models.CharField(max_length=30,)
    department = models.CharField(max_length=50,)
    numberofpc = models.CharField(max_length=20,)
    approvalperson = models.CharField(max_length=20,)
    technician = models.CharField(max_length=20,)
    servicingdate = models.DateField(verbose_name='servicingdate', default=timezone.now())
    remark = models.CharField(max_length=500,)
