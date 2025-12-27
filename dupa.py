import requests
from bs4 import BeautifulSoup

# Funkcja rekurencyjna do przechodzenia po zagnieżdżonych divach
def print_div_map(element, level=0):
    if element.name == 'div':
        print(' ' * level * 2 + f"<div class='{element.get('class')}' id='{element.get('id')}'>")
        for child in element.children:
            if hasattr(child, 'name'):
                print_div_map(child, level + 1)
        print(' ' * level * 2 + "</div>")
    elif element.name == 'a':
        print(' ' * level * 2 + f"<a href='{element.get('href')}'>{element.text.strip()}</a>")

# Pobierz stronę do analizy
def map_divs_on_page(episode_num):
    url = f"https://paldea.pl/anime/hz{episode_num:03d}/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Strona {url} nie istnieje lub jest pusta.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.find('body')

    if body:
        print_div_map(body)
    else:
        print("Nie znaleziono elementu <body>")

# Test na pierwszym odcinku
map_divs_on_page(1)
