import requests
from bs4 import BeautifulSoup
from store_antartica.tasks.scraperAntartica.scraper_list_book import get_list_book
from siteapp.models import CategorysScraper


def go_page_antartica(MAX_PAGES):
    list_general_books = []
    list_general_books_store = []
    categorias = CategorysScraper.objects.filter(store_id=3,id=9)
    for categorys in categorias:
        initial_page = "1"
        params = f'?p={initial_page}&product_list_limit=60'
        url = categorys.url + params
        category_id = categorys.category.id
        print(category_id)
        print(url)
        count = 1
        while url.__contains__("www.antartica.cl"):
            response = requests.get(url)
            if response.status_code == 200:
                html = response.content
            else:
                print("No se pudo obtener el HTML de la página.")
            soup = BeautifulSoup(html, "html.parser")
            # print(soup)
            url = soup.select_one(".next-page")["href"]
            print(dict(next_page=url))
            list_book, list_book_store = get_list_book(url, category_id)
            print(list_book)
            list_general_books += list_book
            list_general_books_store += list_book_store
            count += 1
            if MAX_PAGES and count >= MAX_PAGES:
                break
    return list_general_books, list_general_books_store






    # except:
    #     print("nada")



    # list_url_category = [("Computacion e Informatica",
    #                       f"https://www.antartica.cl/libros/computacion-e-informacion.html?p=?p={initial_page}&product_list_limit=60"),
    #                      ("Mundo Comic",
    #                          f"https://www.antartica.cl/libros/mundo-comic.html?p={initial_page}&product_list_limit=60"),
    #                      ("Literatura",
    #                          f"https://www.antartica.cl/libros/literatura.html?p={initial_page}&product_list_limit=60"),
    #                      ("Infantil y Juvenil",
    #                          f"https://www.antartica.cl/libros/infantil-y-juvenil/libros-infantiles.html?p={initial_page}&product_list_limit=60"),
    #                      ("Viaje y Turismo",
    #                          f"https://www.antartica.cl/libros/guias-de-viaje-y-tur.html?p={initial_page}&product_list_limit=60"),
    #                      ("Cuerpo y Mente",
    #                          f"https://www.antartica.cl/libros/cuerpo-y-mente.html?p={initial_page}&product_list_limit=60"),
    #                      ("Economia y Administracion",
    #                          f"https://www.antartica.cl/libros/economia-y-administracion.html?p={initial_page}&product_list_limit=60"),
    #                      ("Ciencias",
    #                          f"https://www.antartica.cl/libros/ciencias.html?p={initial_page}&product_list_limit=60"),
    #                      ("mas vendidos",
    #                          f"https://www.antartica.cl/mas-vendidos/libros.html?p={initial_page}&product_list_limit=60"),
    #                      ("novedades",
    #                       f"https://www.antartica.cl/novedades/novedades-libros.html?p={initial_page}&product_list_limit=60")
    #                      ]
    # print(list_url_category[0])


# def go_antartica(list_url_category):
#     for url in list_url_category:
#         list_book = []
#         list_book_store = []
#         for page in range(1, 5):
#             #url = f"https://www.antartica.cl/libros/infantil-y-juvenil/libros-infantiles.html?p={page}&product_list_limit=60"
#             category = 'infantil y juvenil'
#             response = requests.get(url)
#             if response.status_code == 200:
#                 html = response.content
#             else:
#                 print("No se pudo obtener el HTML de la página.")

#             soup = BeautifulSoup(html, "html.parser")

#             # books = soup.find_all("div", {"class": "product-item-info"})
#             books = soup.select(".item.product.product-item .product-item-info")
#             #books = books[-1::]
#             print(len(books))
#             for index, book in enumerate(books):
#                 title = book.select_one(".product-item-link").text.strip()
#                 price = book.select_one(".price-wrapper").text.strip()
#                 link = book.select_one(".product.photo.product-item-photo")["href"]
#                 print(link,'linkssss')
#                 response = requests.get(link)
#                 if response.status_code == 200:
#                     html = response.content
#                 else:
#                     print("No se pudo obtener el HTML de la vista del libro.")
#                 soup = BeautifulSoup(html, "html.parser")
#                 book_imagen = soup.select_one(".gallery-placeholder__image")['src']
#                 print(book_imagen, "imagen")
#                 book_title = soup.select_one(".base").text.strip()
#                 print(book_title, "title")
#                 element_editorial = soup.select_one(".link-editorial-search-result")
#                 book_editorial = element_editorial.text.strip() if element_editorial else ''
#                 element_autor = soup.select_one(".link-autor-search-result")
#                 book_autor = element_autor.text.strip() if element_autor else ''
#                 element_isbn = soup.select_one("span.isbn")
#                 book_isbn = element_isbn if element_isbn else None
#                 if not book_isbn:
#                     continue
#                 book_isbn = book_isbn.text.replace("  ", "").replace(":", "")
#                 print(book_isbn, "isbn")
#                 book_price = soup.select_one("span.price").text
#                 book_description = soup.select_one(".accordion-body").text
#                 book_sub_category = soup.select_one(
#                     "span#attr_sub_tema").text.strip()
#                 book_idioma = soup.select_one("span#attr_idioma").text.strip()
#                 element_paginas = soup.find("span", {"id": "attr_n_pagina"})
#                 book_paginas = element_paginas.text.strip() if element_paginas else 0
#                 element_formato = soup.find("span", {"id": "attr_formato"})
#                 book_formato = element_formato.text.strip() if element_formato else ''
#                 element_calificacion = soup.find("span", {"itemprop": "ratingValue"})
#                 book_calificacion = str((int(element_calificacion.text) *5)/100) if element_calificacion else None
#                 # comentarios de los libros
#                 # falta sacar el rating del comentario
#                 item = soup.find("input", {"name": "item"})["value"]
#                 url3 = 'https://www.antartica.cl/review/product/listAjax/id/'+item
#                 print(item)
#                 print(url3)
#                 response = requests.get(url3)
#                 if response.status_code == 200:
#                     html = response.content
#                     print(response)
#                 else:
#                     print("No se pudo obtener el HTML de la página.")

#                 soup = BeautifulSoup(html, "html.parser")
#                 endpoint_none = soup.select_one("div.review-list")
#                 list_comment = []
#                 if endpoint_none != None:
#                     li_comment = soup.select("li.review-item")
#                     print(li_comment,'li_coment')
#                     print(endpoint_none)
#                     for i in li_comment:
#                         nombre = i.select_one(".review-details-value").text.replace('  ','')
#                         descripcion = i.select_one(".review-content").text.replace('  ','')
#                         rating = i.find("span", {"itemprop": "ratingValue"}).text.replace('  ','').replace('%','')
#                         calificacion = (int(rating) *5)/100
#                         print(nombre,'name')
#                         print(descripcion,'descripcion')
#                         print(rating,'rating')
#                         print(calificacion,'calificacion')
#                         list_comment.append({
#                             'name': nombre,
#                             'description': descripcion,
#                             'rating': str(calificacion)
#                         })
#                 print(list_comment)


#
#                 list_book_store.append({
#                     'price': int(limpiar_numeros(book_price)),
#                     'url_book': link,
#                 })
#         return list_book,list_book_store

# #go_antartica()
