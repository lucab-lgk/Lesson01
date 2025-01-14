from django.shortcuts import render
from django.http import HttpResponse
from . import MovieAndActor  # Ton module pour le traitement des données
from . import SummaryOfFilm  # Ton module pour le résumé des films
from . import ListOfFilms

def html(request):
    if request.method == "POST":  # Traiter les données si formulaire soumis
        actor_name = request.POST.get('actorNameInput', '')  # Récupère la valeur du champ "actorNameInput"
        film_name = request.POST.get('filmNameInput', '')    # Récupère la valeur du champ "filmNameInput"
        genre_name = request.POST.get('genreNameInput','')
        genre_result = request.POST.get('genreNameInput','')
        
        # Traitement avec tes modules personnalisés
        actor_result = ListOfFilms.get_movies_by_actor(actor_name, genre_name)
        
        
        summary_result = SummaryOfFilm.nameChange(film_name)

        # Renvoyer les résultats dans une nouvelle page
        return render(request, "results.html", {
            "actor_name": actor_name,
            "actor_result": actor_result,
            "summary_result": summary_result,
            "film_name": film_name,
            "genre_name": genre_name,
            "genre_result": genre_result,
        })

    # Si GET, afficher le formulaire initial
    return render(request, "form.html")