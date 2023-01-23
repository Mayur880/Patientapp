from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=('full_name','email','mobile_no','address','details','preout','visit_date','next_date')

admin.site.register(Patient,PatientAdmin)