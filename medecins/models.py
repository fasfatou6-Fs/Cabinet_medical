from django.db import models

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, default="Inconnu")
    specialite = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField( blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.specialite})"
