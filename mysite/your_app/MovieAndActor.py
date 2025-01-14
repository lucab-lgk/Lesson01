import requests # type: ignore


name = 'Tom Hanks'
def nameChange(x):
    name = x
    return name
    

url = "https://api.themoviedb.org/3/search/person?query="+name+"&include_adult=false&language=en-US&page=1"


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
}


response = requests.get(url, headers=headers)

response2 = response.content.find(1)

json_data = requests.get(url, headers=headers).json()


id = json_data['results'][0]['id']

t = id

url1 = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_people="+str(t)+""

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
}
json_data1 = requests.get(url1, headers=headers).json()
title = json_data1['results'][0]['title']

response1 = requests.get(url1, headers=headers)


print(id)
print(title)

def get_actor_id(actor_name):
    url = f"https://api.themoviedb.org/3/search/person?query={actor_name}&include_adult=false&language=en-US&page=1"
    response = requests.get(url, headers=headers)
    json_data = response.json()
    if 'results' in json_data and json_data['results']:
        return json_data['results'][0]['id']


def get_movies_by_actor(actor_name):
    # Obtenir l'ID de l'acteur
    actor_id = get_actor_id(actor_name)
    # Construire l'URL pour découvrir les films de l'acteur
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_people={actor_id}"
    response4 = requests.get(url, headers=headers)
    data1 = response4.json()

    return data1
    




