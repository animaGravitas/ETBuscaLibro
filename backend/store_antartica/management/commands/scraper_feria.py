from django.core.management.base import BaseCommand
from store_antartica.tasks.scraperFeriaChilenaDelLibro.scraper_feria import go_page_feria
from .scraper_base import save_list_book


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        list_general_books, list_general_books_store = go_page_feria(
            MAX_PAGES=1)
        store_id = 4
        save_list_book(store_id, list_general_books, list_general_books_store)
