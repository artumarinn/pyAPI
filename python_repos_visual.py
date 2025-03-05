import requests
import plotly.express as px

# Realiza una llama a la API y analiza la respuesta
url = "https://api.github.com/search/repositories" # parte principal de la url
url += "?q=language:python+sort:stars+stars:>1000" # cadena de consulta 

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers) # llammada a la api, se asigna el objeto de respuesta a variable r.
print(f"Status code: {r.status_code}")

# Procesa los resultados totales
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Procesa la informacion del repositorio
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Visualizacion
fig = px.bar(x=repo_names, y=stars)
fig.show()
