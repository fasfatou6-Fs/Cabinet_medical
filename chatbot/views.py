from django.shortcuts import render, redirect
from .models import Message
from patients.models import Patient
from medecins.models import Medecin
from rendezvous.models import RendezVous
from datetime import date

def chatbot_home(request):
    response = None

    if request.method == "POST" and "clear" in request.POST:
        Message.objects.all().delete()
        return redirect("chatbot_home")

    if request.method == "POST" and "message" in request.POST:
        user_message = request.POST.get("message").lower()

        # Logique intelligente
        if "bonjour" in user_message or "salut" in user_message:
            response = "Bonjour 👋, je suis votre assistant virtuel. Vous pouvez me demander des infos sur les patients, les rendez-vous ou les médecins."
        elif "j’aimerais avoir des informations" in user_message:
            response = "Bien sûr 😊. Dites-moi ce que vous cherchez : un patient, un médecin, un rendez-vous ou une consultation ?"
        elif "liste des patients" in user_message:
            patients = Patient.objects.all()
            if patients.exists():
                noms = ", ".join([p.nom for p in patients])
                response = f"Voici les patients enregistrés : {noms}"
            else:
                response = "Aucun patient n’est enregistré pour le moment."
        elif "prochain rendez-vous" in user_message:
            rdv = RendezVous.objects.order_by('date').first()
            if rdv:
                response = f"Prochain rendez-vous : {rdv.patient.nom} avec Dr. {rdv.medecin.nom} le {rdv.date.strftime('%d/%m/%Y')}."
            else:
                response = "Aucun rendez-vous n’est prévu."
        elif "médecins disponibles" in user_message:
            medecins = Medecin.objects.all()
            if medecins.exists():
                noms = ", ".join([m.nom for m in medecins])
                response = f"Voici les médecins disponibles : {noms}"
            else:
                response = "Aucun médecin enregistré."
        else:
            response = f"Je suis désolé, je n’ai pas compris. Essayez avec : 'liste des patients', 'prochain rendez-vous', ou 'médecins disponibles'."

        Message.objects.create(user_text=user_message, bot_response=response)

    messages = Message.objects.order_by('-timestamp')[:10]
    return render(request, "chatbot/chatbot_home.html", {
        "response": response,
        "messages": messages
    })