from django.test import TestCase
from .models import Patient
from datetime import date

class PatientModelTest(TestCase):
    def test_create_patient(self):
        patient = Patient.objects.create(
            nom="Diallo",
            prenom="Aminata",
            date_naissance=date(1995, 5, 12)  # ✅ champ obligatoire
        )
        self.assertEqual(patient.nom, "Diallo")
        self.assertEqual(patient.prenom, "Aminata")
        self.assertEqual(patient.date_naissance, date(1995, 5, 12))