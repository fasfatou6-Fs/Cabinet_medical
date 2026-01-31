from django import forms
from .models import RendezVous

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ["patient", "medecin", "date_rendezvous", "heure_rendezvous"]
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'medecin': forms.Select(attrs={'class': 'form-select'}),
            'date_rendezvous': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure_rendezvous': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
        labels = {
            'patient': 'Patient',
            'medecin': 'Médecin',
            'date_rendezvous': 'Date du rendez-vous',
            'heure_rendezvous': 'Heure',
        }