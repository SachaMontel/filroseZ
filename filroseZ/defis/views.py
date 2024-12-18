from django.shortcuts import render
from .models import Defis

# Create your views here.
def index(request):
    if 'table_data' not in request.session:
        request.session['table_data'] = {'1': [], '2': [], '3': [], '4': []}

    if request.method == "POST" and request.user.is_superuser:
        # Récupérer les données du formulaire
        selected_defi = request.POST.get('defi')
        team_column = request.POST.get('team')

        # Ajouter le défi sélectionné à la colonne correspondante
        request.session['table_data'][team_column].append(selected_defi)
        request.session.modified = True

        return redirect('index')

    # Récupérer tous les défis disponibles
    tous_les_defis = Defis.objects.all()
    table_data = request.session['table_data']
    return render(request, 'defis/index.html', {'defis': tous_les_defis, 'table_data': table_data})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def defis(request):
    if request.method == "POST" and request.user.is_superuser:
        # Récupère les données du formulaire
        name = request.POST.get('name')
        pts = request.POST.get('pts')
        
        # Crée un nouvel objet défi
        Defis.objects.create(name=name, pts=pts)
        
        # Redirige pour éviter le rechargement du formulaire
        return redirect('defis')

    # Récupère tous les défis pour affichage
    tous_les_defis = Defis.objects.all()
    return render(request, 'defis/defis.html', {'defis': tous_les_defis})
