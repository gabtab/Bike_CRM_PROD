from django.contrib import admin

# Register your models here.
from .models import Bike
from import_export.admin import ImportExportModelAdmin




class ViewAdmin(ImportExportModelAdmin):
	pass


admin.site.register(Bike, ViewAdmin)