from django import forms
from .models import Medecin

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'specialite', 'telephone', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Spécialité'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'specialite': 'Spécialité',
            'telephone': 'Téléphone',
            'email': 'Email',
        }

        