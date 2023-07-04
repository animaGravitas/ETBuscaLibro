import requests
from bs4 import BeautifulSoup
import re
from store_antartica.tasks.scraperbuscalibre.scraper_view_book import get_view_book_buscalibre


def get_list_book_buscalibre(url, category):
    list_book = []
    list_book_store = []
    try:
        response = requests.get(url)
    except:
        print(url, 'url error')
        return list_book, list_book_store
    if response.status_code == 200:
        html = response.content
    else:
        print("No se pudo obtener el HTML de la página.")

    soup = BeautifulSoup(html, "html.parser")
    next_url = soup.select_one(".pagnNext")["href"]


    # books = soup.find_all("div", {"class": "product-item-info"})
    books = soup.select(".box-producto.producto")
    # books = books[-1::]
    #print(len(books))
    # print(books)
    for index, book in enumerate(books):
        link = book.select_one("a")["href"]
        print(link,'link libro')
        book_imagen = book.select_one("img",{"class" : ".lazyloaded"})['data-src']
        print(book_imagen,'imagen libro')
        book, book_store = get_view_book_buscalibre(link, category)
        # print(get_view_book(link))
        # print(title)
        # print(book_imagen)
        if len(book):
            book.update({
                'image': book_imagen,
            })
            list_book.append(book)
            list_book_store.append(book_store)

    return list_book, list_book_store,next_url

