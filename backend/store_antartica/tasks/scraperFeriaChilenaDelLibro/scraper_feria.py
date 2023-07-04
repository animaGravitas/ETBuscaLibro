import requests
from bs4 import BeautifulSoup
from store_antartica.tasks.scraperFeriaChilenaDelLibro.scraper_list_book import get_list_book_feria
from siteapp.models import CategorysScraper


def go_page_feria(MAX_PAGES):
    list_general_books = []
    list_general_books_store = []
    categorias = CategorysScraper.objects.filter(store_id=4)
    for categorys in categorias:
        url = categorys.url
        category_id = categorys.category.id
        print({category_id})
        print({url})
        count = 1
        while url.__contains__("feriachilenadellibro.cl"):
            response = requests.get(url)
            if response.status_code == 200:
                html = response.content
                # print(html)
            else:
                print("No se pudo obtener el HTML de la página.")
            soup = BeautifulSoup(html, "html.parser")
            # print(soup)
            url = soup.select_one(".next.page-numbers")["href"]
            print(dict(next_page=url))
            list_book, list_book_store = get_list_book_feria(url, category_id)
            print(list_book)
            list_general_books += list_book
            list_general_books_store += list_book_store
            count += 1
            if MAX_PAGES and count >= MAX_PAGES:
                break
    return list_general_books, list_general_books_store


# go_page_antartica(MAX_PAGES=1)
