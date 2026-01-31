from datetime import date
from consultations.models import Consultation
from rendezvous.models import RendezVous

def notifications_context(request):
    today = date.today()

    consultations_today = Consultation.objects.filter(date_consultation=today).count()
    rendezvous_today = RendezVous.objects.filter(date_rendezvous=today).count()

    notifications = []
    if consultations_today > 0:
        notifications.append(f"{consultations_today} consultations prévues aujourd’hui")
    if rendezvous_today > 0:
        notifications.append(f"{rendezvous_today} rendez-vous prévus aujourd’hui")

    return {
        "notifications": notifications,
        "notifications_count": len(notifications),
    }