from django.shortcuts import render
from django.http import JsonResponse
from . import MovieAndActor  # Ton module pour le traitement des données
from . import SummaryOfFilm  # Ton module pour le résumé des films
from . import ListOfFilms

def renderList(request):
    if request.method == "POST":  # Traiter les données si formulaire soumis
        actor_name = request.POST.get('actorNameInput', '')  # Récupère la valeur du champ "actorNameInput"
        film_name = request.POST.get('filmNameInput', '')    # Récupère la valeur du champ "filmNameInput"
        genre_name = request.POST.get('genreNameInput','')
        genre_result = request.POST.get('genreNameInput','')
        vote_average = request.POST.get('vote_average','')
        print(vote_average)
        
        
        
        # Traitement avec tes modules personnalisés
        actor_result = ListOfFilms.get_movies_by_actor(actor_name, genre_name, vote_average)
        

        selected_film = request.POST.get('selectedFilm', '')  # Récupère le film sélectionné
        if selected_film:
            filmSel_name = selected_film
            summarySel_result = SummaryOfFilm.nameChange(filmSel_name)
        else:
            filmSel_name = ""
            summarySel_result = ""

        # Renvoyer les résultats dans une nouvelle page
        return render(request, "resultsList.html", {
            "actor_name": actor_name,
            "actor_result": actor_result,
            "genre_name": genre_name,
            "genre_result": genre_result,
            "summarySel_result": summarySel_result,
            "filmSel_name": filmSel_name,
            "vote_average":vote_average,
            
        })
    # Si GET, afficher le formulaire initial
    return render(request, "form.html")

def renderSumm(request):
    if request.method == "POST":  # Traiter les données si formulaire soumis
      # Récupère la valeur du champ "actorNameInput"
        film_name = request.POST.get('filmNameInput', '')    # Récupère la valeur du champ "filmNameInput"
        vote_average = request.POST.get('vote_average','')
        # Traitement avec tes modules personnalisés
        
        
        summary_result = SummaryOfFilm.nameChange(film_name)
        vote_average = SummaryOfFilm.getVotes(film_name)
        
        
        selected_film = request.POST.get('selectedFilm', '')  # Récupère le film sélectionné
        if selected_film:
            filmSel_name = selected_film
            vote_average = SummaryOfFilm.getVotes(film_name)
            
            summarySel_result = SummaryOfFilm.nameChange(filmSel_name)
        else:
            
            filmSel_name = ""
            summarySel_result = ""

        # Renvoyer les résultats dans une nouvelle page

        return render(request, "resultsSummaryInput.html", {
            "summary_result": summary_result,
            "film_name": film_name,
            "summarySel_result": summarySel_result,
            "filmSel_name": filmSel_name,
            "vote_average":vote_average,
            
        })
    # Si GET, afficher le formulaire initial
    return render(request, "form.html")

def get_movie_summary(request):
    film_title = request.GET.get('title', '')
    summary = SummaryOfFilm.nameChange(film_title),
    votes = SummaryOfFilm.getVotes(film_title),
    # Utiliser la fonction pour obtenir le résumé
    return JsonResponse({'title': film_title, 'summary': summary, 'vote_average':votes})

def html1(request):
    # Si GET, afficher le formulaire initial
    return render(request, "form.html")