from django.shortcuts import render, get_object_or_404, redirect
from .models import Medecin
from .forms import MedecinForm

def medecins_list(request):
    medecins = Medecin.objects.all()
    return render(request, 'medecins/medecins_list.html', {'medecins': medecins})

def medecins_create(request):
    if request.method == "POST":
        form = MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medecins_list')
    else:
        form = MedecinForm()
    return render(request, 'medecins/medecins_form.html', {'form': form})

def medecins_update(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    if request.method == "POST":
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            return redirect('medecins_list')
    else:
        form = MedecinForm(instance=medecin)
    return render(request, 'medecins/medecins_form.html', {'form': form})

def medecins_delete(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    if request.method == "POST":
        medecin.delete()
        return redirect('medecins_list')
    return render(request, 'medecins/medecins_confirm_delete.html', {'medecin': medecin})