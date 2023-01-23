from  django import forms

from patient1.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=('full_name','email','mobile_no','address','details','preout','next_date')