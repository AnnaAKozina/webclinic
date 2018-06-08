from django.contrib import admin
from .models import Owner, Patient, Doctor, Record

admin.site.register(Owner)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Record)

