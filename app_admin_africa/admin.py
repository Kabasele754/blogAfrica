#from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Country, Admin,GestionCulture

#@admin.register(Student)
#class StudentAdmin(ImportExportModelAdmin):
#    pass

admin.site.register(Country)
admin.site.register(Admin)
admin.site.register(GestionCulture)