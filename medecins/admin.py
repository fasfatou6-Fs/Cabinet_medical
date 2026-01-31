from django.contrib import admin
from .models import Medecin

@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ("nom", "specialite")
    search_fields = ("nom",  "specialite")
# Register your models here.



    