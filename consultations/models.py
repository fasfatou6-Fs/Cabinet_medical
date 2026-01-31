from django.db import models

class Consultation(models.Model):
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE, related_name="consultations")
    medecin = models.ForeignKey("medecins.Medecin", on_delete=models.CASCADE, related_name="consultations")
    date_consultation = models.DateField()
    heure = models.TimeField()
    motif = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Consultation de {self.patient} avec {self.medecin} le {self.date_consultation}"