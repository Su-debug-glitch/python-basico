# Ejemplo de una clase
class Coche:
    # atributo de clase -> lo comparten todas las instancias 
    tipo = "vehículo de cuatro ruedas"
    ruedas = 4

    # método que construye el objeto, se llama cuando creas la instancia (CONSTRUCTOR)
    def __init__(self, marca, modelo, color): # self se refiere a sí mismo
        # atributos de la instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} arrancó.")

mi_coche = Coche("Toyota", "Yaris", "negro")
mi_coche.arrancar()
print(mi_coche.marca)

mi_segundo_coche = Coche("Nissan", "350z Tuning", "negro")
mi_segundo_coche.arrancar()
print(mi_segundo_coche.marca)

# Encapsulación: es ocultar los detalles internos de una clase y exponer solo la interfaz pública

# Crear una clase para llamar a la AI de OpenAI, Deepseek, etc

OPENAI_KEY = ""
DEEPSEEK_API_KEY = ""

import requests
class AI_API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {self.api_key}"
        }
        data = {
        "model": self.model,
        "messages": [{"role": "user", "content": prompt}]
        }
        try:
            response = requests.post(self.url, json=data, headers=headers)
            res_json = response.json()
            print(res_json["choices"][0]["message"]["content"])
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None

print("\nOPEN_AI:")
openai_api = AI_API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")

openai_api.call("Escribe un breve poema sobre la programación")

print("\nDEEPSEEK:")
deepseek_api = AI_API(DEEPSEEK_API_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")

deepseek_api.call("Escribe un breve poema sobre la programación")