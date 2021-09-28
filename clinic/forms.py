from django import forms
from django.forms.fields import RegexField, CharField
from django.core.validators import RegexValidator

import re

# reg = re.compile('^[0-9]{5}(?:-[0-9]{4})?$',re.UNICODE)

class ZipcodeForm (forms.Form):
  
    zipcode = forms.CharField(
                            min_length=5,
                            max_length=10,
                            required= True,
                            label='Zipcode', 
                            )

    radius = forms.IntegerField(
                            required= True,
                            label='Radius (in miles)', 
                            ) 