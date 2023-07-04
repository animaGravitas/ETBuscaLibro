from django.contrib import admin
from .models import Book, Store, BookStore, Comments, Categorys, CategorysScraper
from django.utils.html import format_html


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'categorys',
                    'preview_image_small', 'link_image', 'isbn')
    list_per_page = 2000
    ordering = ('-id',)
    search_fields = ('isbn', 'title')
    list_filter = ['categorys']


    def preview_image_small(self, instance):
        str_image = instance.image if instance.image else ''
        return format_html('<a target="_blank" href="' + str_image+'"><img width="120" src="' + str_image + '"/></a>')

    def link_image(self, instance):
        str_image = instance.image if instance.image else ''
        return format_html('<a target="_blank" href="' + str_image+'">' + str_image + '</a>')


admin.site.register(Book, BookAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'web', 'preview_image_small', 'image')
    list_per_page = 200
    ordering = ('-id',)

    def preview_image_small(self, instance):
        str_image = instance.image if instance.image else ''
        return format_html('<a target="_blank" href="' + str_image+'"><img width="120" src="' + str_image + '"/></a>')


admin.site.register(Store, StoreAdmin)


class BookStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'link_url_book', 'store',
                    'price', 'discount', 'get_book_isbn', 'book_id')
    list_per_page = 200
    ordering = ('-id',)
    list_filter = ['store']
    search_fields = ['book__title']

    def link_url_book(self, instance):
        str_url_book = instance.url_book if instance.url_book else ''
        return format_html('<a target="_blank" href="' + str_url_book+'">' + str_url_book + '</a>')

    def get_book_isbn(self, object):
        return object.book.isbn


admin.site.register(BookStore, BookStoreAdmin)


class ComentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_platform_id', 'name',
                    'rating', 'image_url', 'book', 'store', 'get_book_isbn')
    list_per_page = 200
    ordering = ('-id',)

    def get_book_isbn(self, object):
        return object.book_id


admin.site.register(Comments, ComentsAdmin)


class CategorysAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 200
    ordering = ('-id',)


admin.site.register(Categorys, CategorysAdmin)


class CategorysScraperAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_url_category', 'store',
                    'category')
    list_per_page = 200
    ordering = ('-id',)

    def link_url_category(self, instance):
        str_url_page = instance.url if instance.url else ''
        return format_html('<a target="_blank" href="' + str_url_page+'">' + str_url_page + '</a>')


admin.site.register(CategorysScraper, CategorysScraperAdmin)
