from django.db import models

class RendezVous(models.Model):
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, related_name="rendezvous")
    medecin = models.ForeignKey("medecins.Medecin", on_delete=models.CASCADE, related_name="rendezvous")
    date_rendezvous = models.DateField()
    heure_rendezvous = models.TimeField()

    def __str__(self):
        return f"Rendez-vous de {self.patient} avec {self.medecin} le {self.date_rendezvous}"