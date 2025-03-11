import requests # type: ignore
import random



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
        
        
        
        
        


def get_movies_by_actor(x,genre_name,vote_average):
        # Obtenir l'ID de l'acteur
        print(vote_average)
        print(vote_average)
                
        random_page = str(random.randint(1,1))
        print("test")
        print(random_page)
        
        actor_id = get_actor_id(x)
        genre_id = get_genre_id(genre_name)
        
        
        
        # Construire l'URL pour découvrir les films de l'acteur
        if genre_id is None:
            
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
            }
            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={random_page}&sort_by=popularity.desc&vote_average.gte={vote_average}with_people={actor_id}"
            response4 = requests.get(url, headers=headers)
            print(response4)
            data2 = response4.json()
            
            randompage = data2.get('total_pages',1)
            print(randompage)
            
            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={get_random(randompage)}&sort_by=popularity.desc&vote_average.gte={vote_average}with_people={actor_id}"
            
        elif actor_id is None:
            headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
        }
            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={random_page}&sort_by=popularity.desc&vote_average.gte={vote_average}&with_genres={genre_id}"
            
            response4 = requests.get(url, headers=headers)
            print(response4)
            data2 = response4.json()
            
            randompage = data2.get('total_pages',1)
            print(randompage)
            
            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={get_random(randompage)}&sort_by=popularity.desc&sort_by=popularity.desc&vote_average.gte={vote_average}&with_genres={genre_id}"

        elif actor_id is None and genre_id is None:
            headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
        }
            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={random_page}&sort_by=popularity.desc&vote_average.gte={vote_average}"
            
            response4 = requests.get(url, headers=headers)
            print(response4)
            data2 = response4.json()
            
            randompage = data2.get('total_pages',1)
            print(randompage)
            
            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={get_random(randompage)}&sort_by=popularity.desc&vote_average.gte={vote_average}"

        
            
            
        else:
            headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
        }
            #url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={random_page}&sort_by=popularity.desc&with_genres={genre_id}&with_people={actor_id}"
            
            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={random_page}&sort_by=popularity.desc&vote_average.gte={vote_average}&with_genres={genre_id}&with_people={actor_id}"

            #url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.gte=4"

            
            
            response4 = requests.get(url, headers=headers)
            print(response4)
            data2 = response4.json()
            
            randompage = data2.get('total_pages',1)
            print(randompage)
            #url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.gte=8&with_genres=12&with_people=31"

            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={get_random(randompage)}&sort_by=popularity.desc&vote_average.gte={vote_average}&with_genres={genre_id}&with_people={actor_id}"
            print(vote_average)
            
        
        headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
        }
        #response4 = requests.get(url, headers=headers)
        #print(response4)
        #data1 = response4.json()
        
        #print(data1)
        
        response4 = requests.get(url, headers=headers)
        print(response4)
        data1 = response4.json()
            
        randompage = data1.get('total_pages',1)
        print(randompage)
        
        
                
        if genre_id is not None and genre_name:  # genre_name should not be None or empty
            random.shuffle(data1['results'])  # Mélanger les films (présumant que les films sont dans 'results')

            
        film_titles = [movie['original_title'] for movie in data1['results']]

        # Afficher et retourner la liste des titres
        print(genre_name)
        print(genre_id)
        print(film_titles)
        return film_titles
    
    

        
def get_random(number):
    if number>500:
        number = 500
    random_page = str(random.randint(1,number))
    print(random_page)
    return random_page