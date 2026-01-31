from django.shortcuts import render
from .models import Patient 
from .forms import PatientForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages



def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patients_list.html', {'patients': patients})

def patients_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Patient ajouté avec succès.")
            return redirect('patients_list')
    else:
        form = PatientForm()
    return render(request, 'patients/patients_form.html', {'form': form})


def patients_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.info(request, "✏️ Patient modifié avec succès.")
            return redirect('patients_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patients_form.html', {'form': form})

def patients_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.warning(request, "🗑️ Patient supprimé avec succès.")
        return redirect('patients_list')
    return render(request, 'patients/patients_confirm_delete.html', {'patient': patient})


