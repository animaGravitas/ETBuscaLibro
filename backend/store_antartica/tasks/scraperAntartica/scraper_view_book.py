import requests
from bs4 import BeautifulSoup
import re


def limpiar_numeros(cadena):
    return re.sub(r'\D', '', cadena)


def get_view_book(link, category):

    try:
        response = requests.get(link)
    except:
        return {}, {}
    if response.status_code == 200:
        html = response.content
    else:
        print("No se pudo obtener el HTML de la vista del libro.")
    soup = BeautifulSoup(html, "html.parser")
    book_imagen = soup.select_one(".gallery-placeholder__image")['src']
    #print(book_imagen, "imagen")
    book_title = soup.select_one(".base").text.strip()
    #print(book_title, "title")
    element_editorial = soup.select_one(".link-editorial-search-result")
    book_editorial = element_editorial.text.strip() if element_editorial else ''
    #print(book_editorial, 'editorial')
    element_autor = soup.select_one(".link-autor-search-result")
    book_autor = element_autor.text.strip() if element_autor else ''
    #print(book_autor, 'autor')
    element_isbn = soup.select_one("span.isbn")
    book_isbn = element_isbn if element_isbn else None
    if not book_isbn:
        return {}, {}
    book_isbn = book_isbn.text.replace("  ", "").replace(":", "")
    #print(book_isbn, "isbn")
    book_description = soup.select_one(".accordion-body").text
    #print(book_description, 'description')
    book_price = soup.select_one("span.price").text
    #print(book_price, 'price')
    
    element_stock = soup.select_one(".store-available-online")
    book_stock = element_stock.text.strip() if element_stock else ''
    print(book_stock,"book_stock")
    
    element_discount = soup.select_one(".discount-percent-configurable")
    book_discount = element_discount.text.strip() if element_discount else ''
    print(book_discount,"descuntosss")
    
    book_sub_category = soup.select_one(
        "span#attr_sub_tema").text.strip()
    element_idioma = soup.select_one("span#attr_idioma")
    book_idioma = element_idioma.text.strip() if element_idioma else ''
    element_paginas = soup.find("span", {"id": "attr_n_pagina"})
    book_paginas = element_paginas.text.strip() if element_paginas else 0
    element_formato = soup.find("span", {"id": "attr_formato"})
    book_formato = element_formato.text.strip() if element_formato else ''
    element_calificacion = soup.find("span", {"itemprop": "ratingValue"})
    book_calificacion = str(
        (int(element_calificacion.text) * 5)/100) if element_calificacion else None
    # comentarios de los libros
    # falta sacar el rating del comentario
    item = soup.find("input", {"name": "item"})["value"]
    url3 = 'https://www.antartica.cl/review/product/listAjax/id/'+item
    #print(item)
    #print(url3)
    response = requests.get(url3)
    if response.status_code == 200:
        html = response.content
        #print(response)
    else:
        print("No se pudo obtener el HTML de la página.")

    soup = BeautifulSoup(html, "html.parser")
    endpoint_none = soup.select_one("div.review-list")
    list_comment = []
    if endpoint_none != None:
        li_comment = soup.select("li.review-item")
        #print(li_comment, 'li_coment')
        #print(endpoint_none)
        for i in li_comment:
            nombre = i.select_one(
                ".review-details-value").text.replace('  ', '')
            descripcion = i.select_one(
                ".review-content").text.replace('  ', '')
            rating = i.find("span", {"itemprop": "ratingValue"}).text.replace(
                '  ', '').replace('%', '')
            calificacion = (int(rating) * 5)/100
            # print(nombre, 'name')
            # print(descripcion, 'descripcion')
            # print(rating, 'rating')
            # print(calificacion, 'calificacion')
            list_comment.append({
                'name': nombre,
                'description': descripcion,
                'rating': str(calificacion)
            })

    book = {
        'title': book_title,
        'editorial': book_editorial,
        'autor': book_autor,
        'isbn': int(book_isbn),
        'reseña': book_description,
        'categorys_id':  category,
        'sub_category': book_sub_category,
        'formato': book_formato,
        'idioma': book_idioma,
        'pagina': int(book_paginas),
        'calificacion': book_calificacion,
        'list_comment': list_comment
    }

    book_store = {
        'price': int(limpiar_numeros(book_price)),
        'discount': book_discount,
        'url_book': link,
        'stock': book_stock
    }
    return book, book_store
