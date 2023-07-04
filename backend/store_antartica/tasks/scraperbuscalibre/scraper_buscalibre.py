import requests
from bs4 import BeautifulSoup
from store_antartica.tasks.scraperbuscalibre.scraper_list_book import get_list_book_buscalibre
from siteapp.models import CategorysScraper,Categorys


def go_page_buscalibre(MAX_PAGES):
    list_general_books = []
    list_general_books_store = []
    categorias = CategorysScraper.objects.filter(store_id=1)
    for categorys in categorias:
        initial_page = "1"
        params = f'?page={initial_page}'
        url = categorys.url + params
        category_id = categorys.category.id
        print(category_id)
        print(categorys.url,'categorys.url')
        count = 1
        while url.__contains__("www.buscalibre.cl/"):
            print(dict(url=url))
            list_book, list_book_store,url = get_list_book_buscalibre(url, category_id)
            print(list_book,'listbook')
            print(list_book_store,'list_book_store')
            list_general_books += list_book
            list_general_books_store += list_book_store
            count += 1
            if MAX_PAGES and count >= MAX_PAGES:
                break
    return list_general_books, list_general_books_store

