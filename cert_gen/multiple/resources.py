from import_export import resources
from .models import details_csv

class detailscsvresource(resources.ModelResource):
    class Meta:
        model = details_csv