import re
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

# --- Imports ReportLab ---
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from reportlab.lib import colors

# --- Imports Modèles et Formulaires ---
from .models import Consultation
from medecins.models import Medecin 
from .forms import ConsultationForm

# 1. LISTE
@login_required 
def consultations_list(request):
    query = request.GET.get('q', '')
    today = timezone.now().date()
    today_count = Consultation.objects.filter(date_consultation=today).count()
    if query:
        consultations = Consultation.objects.filter(
            Q(patient__nom__icontains=query) | Q(medecin__nom__icontains=query)
        ).order_by('-date_consultation')
    else:
        consultations = Consultation.objects.all().order_by('-date_consultation')
    return render(request, 'consultations/consultations_list.html', {
        'consultations': consultations, 'query': query, 'today_count': today_count
    })

# 2. CRÉATION
@login_required
def consultations_create(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultations_list')
    else:
        form = ConsultationForm()
    return render(request, 'consultations/consultations_form.html', {'form': form})

# 3. MODIFICATION
@login_required
def consultations_update(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            return redirect('consultations_list')
    else:
        form = ConsultationForm(instance=consultation)
    return render(request, 'consultations/consultations_form.html', {'form': form, 'consultation': consultation})

# 4. SUPPRESSION
@login_required
def consultations_delete(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    if request.method == 'POST':
        consultation.delete()
        return redirect('consultations_list')
    return render(request, 'consultations/consultations_confirm_delete.html', {'consultation': consultation})

# 5. GÉNÉRATION PDF - VERSION SÉCURISÉE
@login_required
def generer_ordonnance_pdf(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ordonnance_{consultation.patient.nom}.pdf"'
    
    p = canvas.Canvas(response, pagesize=A5)
    width, height = A5
    
    # Bordure
    p.setStrokeColor(colors.HexColor("#3498DB"))
    p.rect(10, 10, width - 20, height - 20)
    
    # En-tête
    p.setFillColor(colors.HexColor("#2C3E50"))
    p.setFont("Helvetica-Bold", 16)
    p.drawString(40, height - 50, "CABINET MÉDICAL")
    
    # Nom du Docteur
    nom_doc = consultation.medecin.nom if consultation.medecin else "Médecin"
    p.setFont("Helvetica", 10)
    p.drawString(40, height - 65, f"Dr. {str(nom_doc).upper()}")
    p.line(40, height - 80, width - 40, height - 80)
    
    # Patient
    p.setFont("Helvetica-Bold", 12)
    p.drawString(40, height - 110, f"PATIENT : {consultation.patient}")
    
    # Date (Correction AttributeError)
    p.setFont("Helvetica", 10)
    date_val = consultation.date_consultation.strftime('%d/%m/%Y') if consultation.date_consultation else "Date non définie"
    p.drawString(40, height - 125, f"Date : {date_val}")
    
    # Ordonnance
    p.setFont("Helvetica-Bold", 18)
    p.drawCentredString(width/2, height - 180, "ORDONNANCE")
    
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 220, "Prescription :")
    p.drawString(60, height - 245, f"- {consultation.motif}")
    
    # Espace Signature (Correction Medecin object has no attribute 'signature')
    p.setFont("Helvetica-Oblique", 9)
    p.drawString(width - 150, 60, "Signature du médecin :")
    p.line(width - 150, 58, width - 40, 58)
    
    p.showPage()
    p.save()
    return response

# 6. CHATBOT
@csrf_exempt
@login_required
def get_bot_response(request):
    if request.method == "POST":
        message = request.POST.get('message', '').lower()
        if "recap" in message or "récap" in message:
            today = timezone.now().date()
            consultations = Consultation.objects.filter(date_consultation=today)
            count = consultations.count()
            body = f"Bilan du {today}:\nTotal: {count} patients.\n"
            for c in consultations:
                body += f"- {c.patient} (Motif: {c.motif})\n"
            destinataire = request.user.email
            if not destinataire:
                return JsonResponse({'reply': "❌ Email absent du profil."})
            try:
                send_mail("Récapitulatif Médical", body, settings.DEFAULT_FROM_EMAIL, [destinataire])
                return JsonResponse({'reply': f"✅ Envoyé !"})
            except Exception as e:
                return JsonResponse({'reply': f"❌ Erreur : {str(e)}"})
        return JsonResponse({'reply': "Tapez 'recap' pour le bilan."})
    return JsonResponse({'reply': "Invalide."})