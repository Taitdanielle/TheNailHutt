
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import Profile


# Create your models here.
class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, edit)