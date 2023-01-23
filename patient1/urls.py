from django.contrib import admin
from django.urls import path
from .views import index, add_patient, updatePatient, deletePatient, sendEmail

urlpatterns = [
    path('',index ,name='home'),
    path('add_patient/',add_patient,name='addpatient'),
    path('update-patient/<int:id>',updatePatient,name='update-patient'),
    path('delete-patient/<int:id>',deletePatient,name='delete-patient'),
    path('send-email/<int:id>',sendEmail,name='send-email')
]

