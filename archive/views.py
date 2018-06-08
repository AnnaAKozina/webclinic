from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
from datetime import datetime


def index(request):
    all_patients = Patient.objects.all()
    html = ''
    for patient in all_patients:
        url = '/archive/'+str(patient.id) +'/'
        html += '<a href="' +url+ '">'+patient.species+' - '+patient.name+'</a><br>'
    return HttpResponse(html)

def detail(request, patient_id):
    return HttpResponse("<h2>Запись номер: "+str(patient_id)+" </h2>")