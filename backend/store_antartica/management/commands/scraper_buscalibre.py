from django.core.management.base import BaseCommand
from store_antartica.tasks.scraperbuscalibre.scraper_buscalibre import go_page_buscalibre
from .scraper_base import save_list_book


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        list_general_books, list_general_books_store = go_page_buscalibre(
            MAX_PAGES=1)
        store_id = 1
        save_list_book(store_id, list_general_books, list_general_books_store)

        # for index, book in enumerate(list_general_books):
        #     print('holaaa', book)
        #     list_book = Book.objects.filter(isbn=book['isbn'])
        #     list_comment = book.pop('list_comment')
        #     if not list_book.exists():
        #         # Create Book
        #         book_obj = Book.objects.create(**book)
        #         print(book, 'book')
        #     else:
        #         print("else")
        #         book_obj = list_book[0]
        #     if not book_obj.image:
        #         book_obj.image = book['image']

        #     list_bookstore = BookStore.objects.filter(book=book_obj,store_id=store_id   )
        #     if not list_bookstore.exists():
        #         # Create BookStore
        #         data = {
        #             'url_book': list_general_books_store[index]['url_book'],
        #             'price': list_general_books_store[index]['price'],
        #             'discount': list_general_books_store[index]['discount'],
        #             'stock': list_general_books_store[index]['stock'],
        #             'store_id': store_id,
        #             'book_id': book_obj.id
        #         }
        #         book_store_object = BookStore.objects.create(**data)
        #         # Create Comment
        #         for coment in list_comment:
        #             print(coment, 'comment')
        #             comment_object = Comments.objects.create(**{
        #                 'name': coment['name'],
        #                 'description': coment['description'],
        #                 'rating': coment['rating'],
        #                 'store_id': store_id,
        #                 'book_id': book_obj.id

        #             })
        #             print(coment, 'comment')
        #     else:
        #         bookstore_obj = list_bookstore[0]
        #         bookstore_obj.price = list_general_books_store[index]['price']
        #         bookstore_obj.discount = list_general_books_store[index]['discount']
        #         bookstore_obj.stock = list_general_books_store[index]['stock']
        #         bookstore_obj.save()

        #         print("not found", book)
