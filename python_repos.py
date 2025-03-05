import requests

# Realiza una llama a la API y analiza la respuesta
url = "https://api.github.com/search/repositories"
url += "?q=lenguage:python+sort:stars+stars:>1000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convierte el objeto de respuesta en un diccionario
response_dict = r.json()

# Procesa los resultados
print(response_dict.keys())

