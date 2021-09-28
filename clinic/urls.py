# django_clinic_democ/url.py

from django.urls import path , include 
from .views import AboutPageView, search_view, houston_view, laredo_view, pasadena_view, dallas_view, brownsville_view
from django.conf.urls.static import static
from django.conf import settings


# cd into Scripts
# .\activate 
# starts virtual env

urlpatterns = [
    path('', search_view, name='search'),  
    path('houston', houston_view, name='houston'), 
    path('laredo', laredo_view, name='laredo'), 
    path('pasadena', pasadena_view, name='pasadena'), 
    path('dallas', dallas_view, name='dallas'), 
    path('brownsville', brownsville_view, name='brownsville'), 
    path('about', AboutPageView.as_view(), name='about'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)