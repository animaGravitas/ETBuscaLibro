import requests
from bs4 import BeautifulSoup
import re


def limpiar_numeros(cadena):
    return re.sub(r'\D', '', cadena)


def get_view_book(link, category):
    regex = r"<p>Autor:(.*?)<br\/>"
    regex_edi = r"<br/>Editorial:(.*?)<br\/>"

    try:
        response = requests.get(link)
    except:
        return {}, {}
    if response.status_code == 200:
        html = response.content
    else:
        print("No se pudo obtener el HTML de la vista del libro.")
    soup = BeautifulSoup(html, "html.parser")
    book_title = soup.select_one(
        ".product_title.entry-title").text.strip()
    print(dict(title=book_title))

    div_short_description = soup.find(
        "div", class_="woocommerce-product-details__short-description")
    # print(dict(short_description=div_short_description))
    element = str(div_short_description.select_one("p"))
    print(dict(element_autor=element, type=type(element)))
    autor = re.search(regex, element)
    book_autor = autor.groups()[0].strip()
    print(book_autor, 'autor')
    editorial = re.search(regex_edi, element)
    book_editorial = editorial.groups()[0].strip()
    print(book_editorial, 'editorial')

    element_isbn = soup.select_one("span.sku")
    book_isbn = element_isbn if element_isbn else None
    if not book_isbn:
        return {}, {}
    book_isbn = book_isbn.text.replace("  ", "").replace(":", "")
    print(book_isbn, "isbn")

    book_description = soup.select_one(
        ".woocommerce-Tabs-panel.woocommerce-Tabs-panel--description.panel.entry-content.wc-tab").text
    print(book_description, 'description')

    book_price = soup.select_one(".woocommerce-Price-amount.amount").text
    print(book_price, 'price')

    element_stock = soup.select_one(".stock.in-stock")
    book_stock = element_stock.text.strip() if element_stock else ''
    print(book_stock, "book_stock")

    element_discount = soup.select_one(".b_span_text")
    book_discount = element_discount.text.strip() if element_discount else ''
    print(book_discount, "descuntosss")

    element_sub_category = soup.find("a", {"rel": "tag"})
    book_sub_category = element_sub_category.text.strip() if element_sub_category else ''
    print(book_sub_category, 'subcategory')

    element_idioma = soup.find(
        "tr", {"class": "woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_idioma"})
    book_idioma = element_idioma.text.replace(
        'Idioma', '').strip() if element_idioma else ''
    print(book_idioma, 'idioma')

    element_paginas = soup.find(
        "tr", {"class": "woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_paginas"})
    book_paginas = element_paginas.text.replace(
        'Páginas', '').strip() if element_paginas else 0
    print(book_paginas, 'book_paginas')

    element_formato = soup.find(
        "tr", {"class": "woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_pa_encuadernacion"})
    book_formato = element_formato.text.replace(
        'Encuadernación', '').strip() if element_formato else ''
    print(book_formato, 'book_formato')

    element_calificacion = soup.find("span", {"itemprop": "ratingValue"})
    book_calificacion = str(
        (int(element_calificacion.text) * 5)/100) if element_calificacion else None
    # comentarios de los libros
    # falta sacar el rating del comentario

    list_comment = []

    list_comment.append({
        'name': '',
        'description': '',
        'rating': ''
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
