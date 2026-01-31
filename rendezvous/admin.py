from django.contrib import admin
from .models import RendezVous

@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ("patient", "medecin", "date_rendezvous", "heure_rendezvous")
    list_filter = ("date_rendezvous", "medecin")
    search_fields = ("patient__nom", "medecin__nom")


