from datetime import date
from rendezvous.models import RendezVous
from consultations.models import Consultation

def notifications_context(request):
    today = date.today()

    # Compter les rendez-vous et consultations du jour
    rendezvous_today = RendezVous.objects.filter(date_rendezvous=today).count()
    consultations_today = Consultation.objects.filter(date_consultation__date=today).count()

    # Construire la liste des notifications
    notifications = []
    if rendezvous_today > 0:
        notifications.append(f"{rendezvous_today} rendez-vous aujourd’hui")
    if consultations_today > 0:
        notifications.append(f"{consultations_today} consultations prévues aujourd’hui")

    # Retourner les données au template
    return {
        "notifications": notifications,
        "notifications_count": len(notifications)
    }