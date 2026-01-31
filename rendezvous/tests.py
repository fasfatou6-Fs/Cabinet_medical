from django.test import TestCase
from patients.models import Patient
from medecins.models import Medecin
from .models import RendezVous
from datetime import date

class RendezVousModelTest(TestCase):
    def test_create_rendezvous(self):
        patient = Patient.objects.create(
            nom="Konaté",
            prenom="Moussa",
            date_naissance=date(1988, 3, 20)  # ✅ champ obligatoire
        )
        medecin = Medecin.objects.create(nom="Dr Traoré", specialite="Cardiologie")
        rdv = RendezVous.objects.create(patient=patient, medecin=medecin, date=date.today())
        self.assertEqual(rdv.patient.nom, "Konaté")
        self.assertEqual(rdv.medecin.specialite, "Cardiologie")