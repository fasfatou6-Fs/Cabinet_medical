from django.contrib import admin
from .models import Consultation
@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display =("patient", "medecin", "date_consultation", "heure", "motif", "notes")
    list_filter = ("date_consultation", "medecin")
    search_fields = ("patient__nom", "medecin__nom", "motif", "notes")


