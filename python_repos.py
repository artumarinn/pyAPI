import requests

# Realiza una llama a la API y analiza la respuesta
url = "https://api.github.com/search/repositories" # parte principal de la url
url += "?q=language:python+sort:stars+stars:>1000" # cadena de consulta 

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers) # llammada a la api, se asigna el objeto de respuesta a variable r.
print(f"Status code: {r.status_code}")

# Convierte el objeto de respuesta en un diccionario
response_dict = r.json() 

# Procesa los resultados
print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explora la informacion sobre los repositorios
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examina el primer repositorio
repo_dict = repo_dicts[0]

# Extraemos algunos valores de algunas claves del primer diccionario
print("\n Selected information about each repository")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")