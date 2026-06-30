# Scraping -> extraer datos de una web

import requests
import re

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"

response = requests.get(url)

if response.status_code == 200:
    print('La petición fue exitosa')

    html = response.text

    # regex para encontrar el precio
    price_pattern =r'"lowPrice":\s*([0-9]+(?:\.[0-9]{2})?)'
    match = re.search(price_pattern, html)

    if match:
        print(f"El precio del producto es: {match.group(1)}")

