from django.contrib import admin
from .models import Patient
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "date_naissance", "telephone")
    search_fields = ("nom", "prenom", "telephone")
    