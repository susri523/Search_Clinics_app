from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .forms import ZipcodeForm
from .models import Clinic
# from .resources import ClinicResource

from tablib import Dataset

from pyzipcode import ZipCodeDatabase

HOUSTON_CLINICS = Clinic.objects.filter(city="Houston")
BROWNSVILLE_CLINICS = Clinic.objects.filter(city="Brownsville")
PASADENA_CLINICS = Clinic.objects.filter(city="Pasadena")
LAREDO_CLINICS = Clinic.objects.filter(city="Laredo")
DALLAS_CLINICS = Clinic.objects.filter(city="Dallas")


# Create your views here.
class AboutPageView(TemplateView):
    '''inherit from generic templateview'''
    template_name = 'clinic/about.html'

def get_clinic_near_zip(zipcodes):
    possible_clinics = Clinic.objects.filter(zipcode__in=zipcodes)
    return possible_clinics

def search_view(request):
    context = {}
    context['form'] = ZipcodeForm()
    if request.POST:
        zip_from_form = request.POST['zipcode']
        radius_from_form = request.POST['radius']

        zcdb = ZipCodeDatabase()
        try:
            zcdb[zip_from_form]
            context['zipcodes'] = [z.zip for z in zcdb.get_zipcodes_around_radius(zip_from_form, radius_from_form)]
            context['clinics'] = get_clinic_near_zip(context['zipcodes'])

            if context['clinics']:
                return render(request, "clinic/results.html", context )
            else:
                context['error'] = True
                return render(request, "clinic/search.html", context )
        except KeyError:
            context['error'] = True
            return render(request, "clinic/search.html", context )
            
    else: 
        return render(request, "clinic/search.html", context)

def houston_view(request):
    context = {}
    context['clinics'] = HOUSTON_CLINICS
    context['city'] = "Houston"
    return render(request, "clinic/results.html", context )

def dallas_view(request):
    context = {}
    context['clinics'] = DALLAS_CLINICS
    context['city'] = "Dallas"
    return render(request, "clinic/results.html", context )

def pasadena_view(request):
    context = {}
    context['clinics'] = PASADENA_CLINICS
    context['city'] = "Pasadena"
    return render(request, "clinic/results.html", context )

def laredo_view(request):
    context = {}
    context['clinics'] = LAREDO_CLINICS
    context['city'] = "Laredo"
    return render(request, "clinic/results.html", context )

def brownsville_view(request):
    context = {}
    context['clinics'] = BROWNSVILLE_CLINICS
    context['city'] = "Brownsville"
    return render(request, "clinic/results.html", context )