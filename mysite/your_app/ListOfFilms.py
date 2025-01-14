import requests # type: ignore




def get_actor_id(actor_name):
        url = f"https://api.themoviedb.org/3/search/person?query={actor_name}&include_adult=false&language=en-US&page=1"
        headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
        }
        response = requests.get(url, headers=headers)
        json_data = response.json()
        if 'results' in json_data and json_data['results']:
            return json_data['results'][0]['id']
        
def get_genre_id(genre):
        url = f"https://api.themoviedb.org/3/genre/movie/list?language=en"
        headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
        }
        response = requests.get(url, headers=headers)
        json_data = response.json()
        
        if 'genres' in json_data:
                # Parcourir les genres pour trouver une correspondance
                for item in json_data['genres']:
                    if item['name'].lower() == genre.lower():  # Comparaison insensible à la casse
                        return item['id']
        
        
        
        
        


def get_movies_by_actor(x,genre_name):
        # Obtenir l'ID de l'acteur
        actor_id = get_actor_id(x)
        genre_id = get_genre_id(genre_name)
        # Construire l'URL pour découvrir les films de l'acteur
        #url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_people={actor_id}"
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres={genre_id}&with_people={actor_id}"
        headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
        }
        response4 = requests.get(url, headers=headers)
        data1 = response4.json()
        
        
        film_titles = [movie['original_title'] for movie in data1['results']]

        # Afficher et retourner la liste des titres
        print(genre_name)
        print(genre_id)
        print(film_titles)
        return film_titles
