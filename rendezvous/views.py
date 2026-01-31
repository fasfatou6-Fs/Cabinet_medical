from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import RendezVous
from .forms import RendezVousForm

# Liste des rendez-vous
def rendezvous_list(request):
    rendezvous = RendezVous.objects.all()
    query = request.GET.get('q')
    if query:
        rendezvous = rendezvous.filter(
            patient__nom__icontains=query
        ) | rendezvous.filter(
            medecin__nom__icontains=query
        )
    return render(request, 'rendezvous/rendezvous_list.html', {
        'rendezvous': rendezvous,
        'query': query,
    })

# Créer un rendez-vous
def rendezvous_create(request):
    if request.method == "POST":
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rendez-vous ajouté avec succès.")
            return redirect('rendezvous_list')
    else:
        form = RendezVousForm()
    return render(request, 'rendezvous/rendezvous_form.html', {'form': form})

# Modifier un rendez-vous
def rendezvous_update(request, pk):
    rendezvous = get_object_or_404(RendezVous, pk=pk)
    if request.method == "POST":
        form = RendezVousForm(request.POST, instance=rendezvous)
        if form.is_valid():
            form.save()
            messages.success(request, "Rendez-vous mis à jour avec succès.")
            return redirect('rendezvous_list')
    else:
        form = RendezVousForm(instance=rendezvous)
    return render(request, 'rendezvous/rendezvous_form.html', {'form': form})

# Supprimer un rendez-vous
def rendezvous_delete(request, pk):
    rendezvous = get_object_or_404(RendezVous, pk=pk)
    if request.method == "POST":
        rendezvous.delete()
        messages.success(request, "Rendez-vous supprimé avec succès.")
        return redirect('rendezvous_list')
    return render(request, 'rendezvous/rendezvous_confirm_delete.html', {'rendezvous': rendezvous})