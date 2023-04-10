import requests
from bs4 import BeautifulSoup

def find_text(message):
    url = f'https://9v.ru/search?q={message.text}&lang=ru'
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='product-preview__content')
    return quotes