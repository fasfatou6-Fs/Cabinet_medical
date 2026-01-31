from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ["patient", "medecin", "date_consultation", "heure", "motif", "notes"]
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'medecin': forms.Select(attrs={'class': 'form-select'}),
            'date_consultation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'motif': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'patient': 'Patient',
            'medecin': 'Médecin',
            'date_consultation': 'Date de la consultation',
            'heure': 'Heure',
            'motif': 'Motif',
            'notes': 'Notes',
        }