from django.test import TestCase
from django.urls import reverse
from patients.models import Patient
from medecins.models import Medecin
from rendezvous.models import RendezVous
from datetime import date

class ChatbotViewTest(TestCase):

    def test_chatbot_home_post_liste_patients(self):
        """Test affichage de la liste des patients"""
        Patient.objects.create(nom="Diallo", prenom="Aminata", date_naissance=date(1995, 5, 12))
        Patient.objects.create(nom="Konaté", prenom="Moussa", date_naissance=date(1988, 3, 20))
        response = self.client.post(reverse("chatbot_home"), {"message": "liste des patients"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Diallo")
        self.assertContains(response, "Konaté")

    def test_chatbot_home_post_prochain_rendezvous(self):
        """Test affichage du prochain rendez-vous"""
        patient = Patient.objects.create(nom="Traoré", prenom="Fatou", date_naissance=date(2000, 7, 15))
        medecin = Medecin.objects.create(nom="Dr Keita", specialite="Pédiatrie")
        RendezVous.objects.create(patient=patient, medecin=medecin, date=date.today())
        response = self.client.post(reverse("chatbot_home"), {"message": "prochain rendez-vous"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Traoré")
        self.assertContains(response, "Dr Keita")