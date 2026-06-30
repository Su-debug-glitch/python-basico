from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'
headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print('La petición fue exitosa')

    soup = BeautifulSoup(response.text, 'html.parser')

    title_tag = soup.title
    if title_tag:
        print(f"El título de la web es: {title_tag.text}")


    # Adaptado al html actual, NO USANDO EL MISMO CÓDIGO DE @midudev
    # Extraer el precio general del producto desde el JSON-LD 
    price_match = re.search(r'"lowPrice":\s*([0-9]+(?:\.[0-9]{2})?)', response.text)
    price = price_match.group(1) if price_match else 'No disponible'
    print(f"Precio base: {price} €")

    # find each product and get the name and the price
    products = soup.select('.product-selection-1-group .selection-buttons .item')
    for product in products:
        name = product.get_text(' ', strip=True)
        print(f"Producto: {name} | Precio base: {price} €")
