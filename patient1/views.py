from django.http import response
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PatientForm
from .models import Patient
from django.core.mail import send_mail

# Create your views here.

def index(request):
    data = Patient.objects.all()
    return render(request, 'index.html', {'data': data})


# adding Patient

def add_patient(request):
    form = PatientForm
    if request.method == 'POST':
        saveForm = PatientForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request, "data has been saved")
        # else:
        #     messages.error(request, "data invalid")

    return render(request, 'add-patient.html', {'form': form,})


#update Patinnt

def updatePatient(request,id):
    patient=Patient.objects.get(id=id)
    if request.method=='POST':
        saveForm=PatientForm(request.POST,instance=patient)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request,'Data has been updated.')
    form=PatientForm(instance=patient)
    return render(request,'update-patient.html',{'form':form})


def deletePatient(request,id):
    Patient.objects.filter(id=id).delete()
    return redirect('/')

def sendEmail(request,id):
    patient=Patient.objects.get(id=id)
    send_mail(
        'Next Visit Reminder',
        'Your next visit is on ' + str(patient.next_date ),
        'admin@example.com',
        [patient.email],
        fail_silently=False,
    )
    messages.success(request, 'Mail has been sent.')
    return redirect('/')