import requests
from bs4 import BeautifulSoup
import re
from store_antartica.tasks.scraperFeriaChilenaDelLibro.scraper_view_book import get_view_book


def get_list_book_feria(url, category):
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
    # print({soup})
    # books = soup.find_all("div", {"class": "product-item-info"})
    books = soup.select(".purchasable.product-type-simple")
    # books = books[-1::]
    print(len(books))
    for index, book in enumerate(books):
        link = book.select_one(
            ".woocommerce-LoopProduct-link.woocommerce-loop-product__link")["href"]
        print(dict(link_libro=link))
        book_imagen = book.select_one(
            ".attachment-woocommerce_thumbnail.size-woocommerce_thumbnail")['src']
        print(dict(imagen_libro=book_imagen))
        book, book_store = get_view_book(link, category)
        # print(get_view_book(link))
        # print(title)
        # print(book_imagen)
        if len(book):
            book.update({
                'image': book_imagen,
            })
            list_book.append(book)
            list_book_store.append(book_store)

    return list_book, list_book_store
