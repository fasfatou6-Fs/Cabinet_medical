from django.test import TestCase
from patients.models import Patient
from medecins.models import Medecin
from consultations.models import Consultation
from datetime import date

class ConsultationModelTest(TestCase):
    def test_create_consultation(self):
        patient = Patient.objects.create(nom="Camara", prenom="Mariama", date_naissance=date(1990, 4, 10))
        medecin = Medecin.objects.create(nom="Dr Coulibaly", specialite="Dermatologie")
        consultation = Consultation.objects.create(patient=patient, medecin=medecin, date=date.today(), notes="Allergie cutanée")
        self.assertEqual(consultation.patient.nom, "Camara")
        self.assertEqual(consultation.medecin.specialite, "Dermatologie")
        self.assertIn("Allergie", consultation.notes)