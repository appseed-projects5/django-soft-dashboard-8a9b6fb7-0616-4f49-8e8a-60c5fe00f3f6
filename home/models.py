# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Dealers(models.Model):

    #__Dealers_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    logotype = models.CharField(max_length=255, null=True, blank=True)
    term = models.CharField(max_length=255, null=True, blank=True)

    #__Dealers_FIELDS__END

    class Meta:
        verbose_name        = _("Dealers")
        verbose_name_plural = _("Dealers")


class Customer(models.Model):

    #__Customer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Estimate(models.Model):

    #__Estimate_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    createdby = models.CharField(max_length=255, null=True, blank=True)

    #__Estimate_FIELDS__END

    class Meta:
        verbose_name        = _("Estimate")
        verbose_name_plural = _("Estimate")


class Order(models.Model):

    #__Order_FIELDS__
    satstus = models.CharField(max_length=255, null=True, blank=True)

    #__Order_FIELDS__END

    class Meta:
        verbose_name        = _("Order")
        verbose_name_plural = _("Order")


class Estimatedetail(models.Model):

    #__Estimatedetail_FIELDS__

    #__Estimatedetail_FIELDS__END

    class Meta:
        verbose_name        = _("Estimatedetail")
        verbose_name_plural = _("Estimatedetail")


class Brand(models.Model):

    #__Brand_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Brand_FIELDS__END

    class Meta:
        verbose_name        = _("Brand")
        verbose_name_plural = _("Brand")


class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Variantspermanet(models.Model):

    #__Variantspermanet_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Variantspermanet_FIELDS__END

    class Meta:
        verbose_name        = _("Variantspermanet")
        verbose_name_plural = _("Variantspermanet")


class Variantoption(models.Model):

    #__Variantoption_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Variantoption_FIELDS__END

    class Meta:
        verbose_name        = _("Variantoption")
        verbose_name_plural = _("Variantoption")



#__MODELS__END
