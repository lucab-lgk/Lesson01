import requests  # type: ignore

def getVotes(x):

    url = f"https://api.themoviedb.org/3/search/movie?query={x}&include_adult=false&language=en-US&page=1"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTcyNzc3NTk5MC40NTEsInN1YiI6IjY2ZmJjNGY2OGFhNzM0YjM3NmE2NmY5ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BeD2qlKPpNtEW2cVPiYhoDKnxy6fgq13EWAe0sqfM4o"
    }

    response = requests.get(url, headers=headers)
    json_data = response.json()
    if 'results' in json_data and json_data['results']:
        
        vote = json_data['results'][0]['vote_average']
        print(vote)
        return vote
        
    
    print(json_data)
    
def nameChange(x):
    # Si x est None ou vide, ne pas effectuer la requête et retourner une valeur vide.
    if not x:
        print("No query provided.")
        return None

    # Construire l'URL avec le paramètre de recherche
    url = f"https://api.themoviedb.org/3/search/movie?query={x}&include_adult=false&language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
    }

    # Effectuer la requête
    response = requests.get(url, headers=headers)

    # Vérifier si la réponse contient des résultats
    if response.status_code != 200:
        print("Error fetching data from API.")
        return None

    json_data = response.json()

    # Vérifier si la clé 'results' existe et n'est pas vide
    if 'results' in json_data and json_data['results']:
        
        overview = json_data['results'][0]['overview']
        print(overview)
        return overview
    else:
        print("No results found.")
        return None
