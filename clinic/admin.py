from django.contrib import admin
from .models import Clinic

from import_export.admin import ImportExportModelAdmin 


# Register your models here.
@admin.register(Clinic)

class ClinicAdmin(ImportExportModelAdmin):
    pass