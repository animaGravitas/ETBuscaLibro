import requests
from bs4 import BeautifulSoup
import re


def limpiar_numeros(cadena):
    return re.sub(r'\D', '', cadena)


def limpiar_rating(cadena):
    regex = r"-(\d)"
    return re.search(regex, cadena)


def get_view_book_buscalibre(link, category):

    try:
        response = requests.get(link)
    except:
        return {}, {}
    if response.status_code == 200:
        html = response.content
    else:
        print("No se pudo obtener el HTML de la vista del libro.")
    soup = BeautifulSoup(html, "html.parser")

    book_title = soup.select_one(".tituloProducto").text.strip()
    print(book_title, "title")
    element_editorial = soup.find("div", {"id": "metadata-editorial"})
    book_editorial = element_editorial.text.strip() if element_editorial else ''
    print(book_editorial, 'editorial')
    element_autor = soup.find("div", {"id": "metadata-autor"})
    book_autor = element_autor.text.strip() if element_autor else ''
    print(book_autor, 'autor')
    element_description = soup.select_one(
        ".descripcionBreve .font-weight-light.font-size-small")
    book_description = element_description.text.strip() if element_description else ''
    print(book_description, 'description')
    element_sub_category = soup.find("div", {"id": "metadata-categorías"})
    book_sub_category = element_sub_category.text.replace(
        "  ", "") if element_sub_category else ''
    print(book_sub_category, 'sub caegory')
    element_idioma = soup.find("div", {"id": "metadata-idioma"})
    book_idioma = element_idioma.text.strip() if element_idioma else ''
    print(book_idioma, 'idioma')
    element_paginas = soup.find("div", {"id": "metadata-número páginas"})
    book_paginas = element_paginas.text.strip() if element_paginas else 0
    print(book_paginas, 'paginas')
    element_formato = soup.find("div", {"id": "metadata-encuadernación"})
    book_formato = element_formato.text.strip() if element_formato else ''
    print(book_formato, 'formato')
    element_calificacion = soup.select_one(".small.stars")["class"][2]
    print(element_calificacion, 'calificacion libro')
    s = limpiar_rating(element_calificacion)
    print(int(s.group()[1::]), 'calificacion limpia')
    book_calificacion_group = int(s.group()[1::])
    book_calificacion = book_calificacion_group if book_calificacion_group else None
    element_isbn = soup.select_one("#metadata-isbn13")
    book_isbn = element_isbn if element_isbn else None
    if not book_isbn:
        return {}, {}
    book_isbn = book_isbn.text.replace("  ", "").replace(":", "")
    print(book_isbn, "isbn")
    element_price = soup.select_one(".precioAhora")
    book_price = element_price if element_price else 0
    if not book_price:
        return {}, {}
    book_price = book_price.text
    print(book_price, 'price')

    element_stock = soup.select_one(
        ".font-size-small.color-green.margin-right-10.margin-bottom-10")
    book_stock = element_stock.text.strip() if element_stock else ''
    print(book_stock, "book_stock")

    element_discount = soup.select_one(".box-descuento")
    book_discount = element_discount.text.strip() if element_discount else ''
    print(book_discount, 'descunto')

    # comentarios de los libros
    # falta sacar el rating del comentario

    endpoint_none = soup.select_one(".row.reviews-body")
    list_comment = []
    if endpoint_none != None:
        em_comment = soup.select("em")
        # print(em_comment, 'em_comment')
        # print(endpoint_none)
        for i in em_comment:
            nombre = i.select_one(
                ".sprite-detalle-before").text.replace('  ', '')
            print(nombre, 'nombre')
            descripcion = i.select_one(".font-weight-normal").text
            print(descripcion, 'descripcion')
            rating = i.select_one(
                "span", {"class": "small.stars.stars-5"})["class"][2]
            s = limpiar_rating(rating)
            print(rating, 'rating')
            print(int(s.group()[1::]), 'sss')
            calificacion = int(s.group()[1::])
            print(calificacion, 'calificacion')
            list_comment.append({
                'name': nombre,
                'description': descripcion,
                'rating': str(calificacion)
            })

    book = {
        'title': book_title,
        'isbn': int(book_isbn),
        'categorys_id':  category,
        'editorial': book_editorial,
        'autor': book_autor,
        'reseña': book_description,
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
