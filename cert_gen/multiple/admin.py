from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from multiple.models import details_csv,civil_details,comp_details,mech_details,elec_details

@admin.register(details_csv)
@admin.register(civil_details)
@admin.register(mech_details)
@admin.register(comp_details)
@admin.register(elec_details)

class SongRankAdmin(ImportExportModelAdmin):
    list_display = ('verify_id', 'name', 'program', 'year', 'tx_rc')

