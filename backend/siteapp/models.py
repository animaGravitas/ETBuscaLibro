from django.db import models
from django.utils import timezone

# choices_category = (
#     ('Computacion e Informatica', 'Computación e Informática'),
#     ('Mundo Comic', 'Mundo Comic'),
#     ('Literatura', 'Literatura'),
#     ('Infantil y Juvenil', 'Infantil y Juvenil'),
#     ('Viaje y Turismo', 'Viaje y Turismo'),
#     ('Cuerpo y Mente', 'Cuerpo y Mente'),
#     ('Economia y Administracion', 'Economía y Administración'),
#     ('Ciencias', 'Ciencias'),
#     ('mas vendidos', 'Mas Vendidos'),
#     ('novedades', 'Novedades')
# )

class Categorys(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Category'
        verbose_name = 'Category'

    def __str__(self):
        return '{}'.format(self.name)


class Book(models.Model):
    id = models.AutoField(primary_key=True, default=None,
                          null=None, blank=None)
    title = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    image = models.URLField(
        max_length=300, default=None, null=True, blank=True)
    editorial = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    autor = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    isbn = models.BigIntegerField(
        help_text='codigo del libro', default=None, null=True, blank=True)
    reseña = models.TextField(default=None, null=True, blank=True)
    categorys = models.ForeignKey(
        Categorys, on_delete=models.SET_NULL, null=True, default=None)
    sub_category = models.CharField(
        verbose_name='sub-Categoria', max_length=40, default=None, null=True, blank=True)
    formato = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    idioma = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    pagina = models.IntegerField(default=None, null=True, blank=True)
    calificacion = models.CharField(
        verbose_name="rating", max_length=200, help_text="rating: 5", default=0, blank=True, null=True,)

    class Meta:
        db_table = 'book'
        verbose_name_plural = 'Books'
        verbose_name = 'Book'

    def __str__(self):
        return '{} {}'.format(self.title, self.id)


class Store(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(verbose_name='web store', max_length=400)
    image = models.URLField(
        max_length=300, default=None, null=True, blank=True)

    class Meta:
        db_table = 'store'
        verbose_name_plural = 'Stores'
        verbose_name = 'Store'

    def __str__(self):
        return '{} {}'.format(self.name, self.web)


class BookStore(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.SET_NULL,
        null=True
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.SET_NULL,
        null=True
    )
    url_book = models.URLField(
        verbose_name='url book', max_length=400, default='')
    price = models.FloatField(
        verbose_name='Precio del libro', null=True, blank=True, default=None)
    discount = models.CharField(max_length=50,
        verbose_name='descuento del libro', null=True, blank=True, default=None)
    stock = models.CharField(max_length=100,
        verbose_name='stock libro en la tienda', null=True, blank=True, default=None)


class Comments(models.Model):
    comment_platform_id = models.CharField(
        verbose_name='Id comentario en plataforma', max_length=20, default=None, null=True)
    name = models.CharField(max_length=300)
    image_url = models.URLField(
        verbose_name='Imagen Medium', default='https://cdn-icons-png.flaticon.com/512/6378/6378141.png', null=True, blank=True)
    description = models.TextField()
    rating = models.CharField(
        verbose_name='evaluacion del curso', max_length=300)
    book = models.ForeignKey(
        Book,
        on_delete=models.SET_NULL,
        null=True
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        db_table = 'comment'
        verbose_name_plural = 'Comments'
        verbose_name = 'Comment'

    def __str__(self):
        return '{} {}'.format(self.name, self.rating)


class CategorysScraper(models.Model):
    url = models.URLField()
    store = models.ForeignKey(
        Store, on_delete=models.SET_NULL, null=True, default=None)
    category = models.ForeignKey(
        Categorys, help_text='my category', on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        db_table = 'category scraper'
        verbose_name_plural = 'Category Scraper'
        verbose_name = 'Category Scraper'


