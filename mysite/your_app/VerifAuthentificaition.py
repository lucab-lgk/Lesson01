import requests # type: ignore

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjRjODI0M2FlZTJmOTBkNGRlOTBlYzFhNWYyMjJiZiIsIm5iZiI6MTczMjAwOTQzNC4zNDg3MjcyLCJzdWIiOiI2NmZiYzRmNjhhYTczNGIzNzZhNjZmOWUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.ALd7Ps3igocwTL5NoHKi5g43HRMjiF52uW1sp9ZrwDE"
}

response = requests.get(url, headers=headers)

print(response.text)