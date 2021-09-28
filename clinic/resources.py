from import_export import resources
from .models import Clinic

class ClinicResource(resources.ModelResource):
    class Meta:
        model = Clinic
        fields = ['id', 'name', 'address', 'zipcode', 'phone', 'website', 'notes']
