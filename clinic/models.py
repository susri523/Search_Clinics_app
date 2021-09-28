from django.db import models
from django.urls import reverse
# from django.contrib import admin
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

zipcode_validator = RegexValidator(regex="^[0-9]{5}(?:-[0-9]{4})?$")


# Create your models here.
class Clinic(models.Model):
    name = models.TextField(blank=True)
    address = models.TextField(blank=True)
    zipcode = models.TextField(blank=True, validators=[zipcode_validator])
    # phone = PhoneNumberField(blank=True)
    city = models.TextField(blank=True)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)


    def __str__(self):
        return f'{self.name}'

