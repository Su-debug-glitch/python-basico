# Hacer peticiones a APIs sin dependencias
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts/"
try:
    response = urllib.request.urlopen(api_posts)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)

    response.close()
except urllib.error.URLError as e:
    print(f"Error en la solicitid: {e}")

# Con dependencia (requests)
import requests
print("\nGET:")
response = requests.get(api_posts)

# POST
print("\nPOST:")
try:
    input = {
        "title": "su",
        "body": "aprendiendo python",
        "userID": 8
    }
    response = requests.post(api_posts, json=input)
    response.status_code # 201 - creado con éxito
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# PUT
print("\nPUT:")
try:
    input = {
        "title": "foo",
        "body": "fighters",
        "userID": 8,
    }
    response = requests.put("https://jsonplaceholder.typicode.com/posts/8", json=input)
    print(response.status_code) # 200 - éxito
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# Usar la API de GPT-4 o de OpenAI
# Ref: https://platform.openai.com/docs/api-reference/making-requests
# solo como prueba, no funciona porque no lo estoy pagando

OPENAI_KEY = "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"

def call_openai_gpt(api_key, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2)) # para mostrarlo más estructurado

print(api_response["choices"][0]["message"]["content"]) # muestra solo el poema

# Llamar a la API de DEEPSEEK -> solo como prueba, no tengo cuenta de deepseek
"""
import json

def call_deepseek(api_key, prompt):
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.json())
    return response.json()

api_response = call_deepseek(DEEPSEEK_API_KEY, "Escribe un breve poema sobre la programación")

# print(json.dumps(api_response, indent=2))

print(api_response["choices"][0]["message"]["content"])

"""