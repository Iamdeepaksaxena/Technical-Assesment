
# Register your models here.
from django.contrib import admin
from .models import Patient, Appointment
from django.contrib import admin
from .models import Patient, Appointment


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'gender', 'blood_group']
    search_fields = ['name', 'contact_number']
    list_filter = ['gender', 'blood_group']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'doctor_name', 'appointment_date', 'status']
    search_fields = ['doctor_name', 'patient__name']
    list_filter = ['status', 'appointment_date']