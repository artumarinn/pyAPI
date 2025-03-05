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
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Convierte los nombres del repositorio en enlaces activos
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Construye los textos emergentes.
    
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text) # añade el texto emergente dentro del bucle

# Visualizacion
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()

