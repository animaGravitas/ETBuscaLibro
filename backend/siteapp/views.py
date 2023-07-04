from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BookSerializer, BookCategorySerializer, BookListCategorySerializer,PaginationsSerializers,CommentSerializer,CommentSerializerGet,BookListCategorySerializer1
from .models import Book, BookStore, Store, Comments, Categorys
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.decorators import action
from django.http import JsonResponse
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from users.models import CustomUser, Comment
from django.http import JsonResponse
import json
from rest_framework import status




class BookDetailView(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        bookstores = BookStore.objects.filter(book=book)
        list_comments = Comments.objects.filter(book_id=book.id)
        categories = Categorys.objects.filter(book=book)
        print(categories, 'categorys')
        print(bookstores, len(bookstores))
        data = {
            'image': book.image,
            'title': book.title,
            'autor': book.autor,
            'editorial': book.editorial,
            'isbn': book.isbn,
            'reseña': book.reseña,
            'categorys': [{'name': cts.name, 'id': cts.id}for cts in categories],
            'sub_category': book.sub_category,
            'formato': book.formato,
            'idioma': book.idioma,
            'pagina': book.pagina,
            'calificacion': book.calificacion,
            'stores': [{'image': bs.store.image, 'price': bs.price, 'stock':bs.stock, 'discount': bs.discount, 'web': bs.store.web, 'url_book': bs.url_book}for bs in bookstores],
            'comments': [{
                'image': comment.image_url,
                'rating': comment.rating,
                'name': comment.name,
                'description': comment.description
            }
                for comment in list_comments],
        }

        print(book)
        print(type(book.calificacion), 'calificacion')
        print(data)
        print('cd')
        return Response(data)


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer
    #permission_classes = [permissions.IsAuthenticated]


class BookCategory(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookCategorySerializer

    @action(detail=False)
    def category(self, request, category=None):
        recent_users = Book.objects.all()
        print('entry', category)

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)


class MyModelPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookCategoryView(APIView):
    def get(self, request, category=None):
        param_pricemin = request.GET.get('pricemin')
        param_pricemax = request.GET.get('pricemax')
        print(param_pricemin,"price min")
        print(param_pricemax,"price max")
        if param_pricemax  and param_pricemax:   
            books = Book.objects.filter(
            categorys=category,
            bookstore__price__gte=int(param_pricemin),
            bookstore__price__lte=int(param_pricemax)
        )
        else:
            books = Book.objects.filter(categorys=category)
        
        for book in books:
            bookstore = list(BookStore.objects.filter(book=book).order_by('price'))
            book.bookStore = [bookstore[0]]
            
        paginator = MyModelPagination()
        page = paginator.paginate_queryset(books, request)
        print('algo')
        serializer = BookListCategorySerializer1(page, many=True)

        return paginator.get_paginated_response(serializer.data)

class BookListCategory(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False)
    def category(self, request, category=None):
        recent_users = Book.objects.all()
        print('entry', category)

        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)


class ListCategoryMundoComic(APIView):
    def get(self, request, category=2):
        books = Book.objects.filter(categorys=category)[:20]
        print('algo')
        serializer = BookListCategorySerializer(books, many=True)
        return Response(serializer.data)


class ListCategoryComputacionInformatica(APIView):
    def get(self, request, category=1):
        books = Book.objects.filter(categorys=category)[:20]
        print('algo')
        serializer = BookListCategorySerializer(books, many=True)
        return Response(serializer.data)


class ListCategoryLiteratura(APIView):
    def get(self, request, category=3):
        books = Book.objects.filter(categorys=category)[:20]
        print('algo')
        serializer = BookListCategorySerializer(books, many=True)
        return Response(serializer.data)


class ListCategoryInfantil(APIView):
    def get(self, request, category=4):
        books = Book.objects.filter(categorys=category)[:20]
        print('algo')
        serializer = BookListCategorySerializer(books, many=True)
        return Response(serializer.data)


class ListCategoryNovedades(APIView):
    def get(self, request, category=10):
        books = Book.objects.filter(categorys=category)[:20]
        print('algo')
        serializer = BookListCategorySerializer(books, many=True)
        return Response(serializer.data)


class ListCategoryvendidos(APIView):
    def get(self, request, category=9):
        books = Book.objects.filter(categorys=category)[:20]
        print('algo')
        serializer = BookListCategorySerializer(books, many=True)
        return Response(serializer.data)


class ListCategoryciencias(APIView):
    def get(self, request, category=8):
        books = Book.objects.filter(categorys=category)[:20]
        print('algo')
        serializer = BookListCategorySerializer(books, many=True)
        return Response(serializer.data)


class SearchBoook(APIView):
    def get(self, request ):
        title_isbn = request.GET.get("search")
        category_id = request.GET.get("category_id")

        books = []
        if title_isbn:
            try:
                is_isbn = bool(int(title_isbn))

            except:
                is_isbn = False


            if is_isbn:
                books = Book.objects.filter(Q(isbn=title_isbn))

            else:
                books = Book.objects.filter(Q(title__icontains=title_isbn))
        if category_id:
             books = Book.objects.filter(Q(categorys_id=category_id))
        serializer = BookListCategorySerializer(books, many=True)
        serializer_result = PaginationsSerializers({'books' : serializer.data, 'count': len(serializer.data)})
        return Response(serializer_result.data)
            

class IsAuthenticatedView(APIView):
    """def get(self, request):
        User = get_user_model()
        authenticated = request.user.is_authenticated
        username = request.user.username if authenticated else None
        data = {
            'authenticated': authenticated,
            'username': username
        }
        return Response(data)"""
    def get(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT')
        cookies = request.COOKIES
        data = {
            'user_agent': user_agent,
            'cookies': cookies
        }
        return JsonResponse(data)
    
class favorite(APIView):
    def post(self, request):
        try:
            payload = json.loads(request.body)
            username = payload.get('username', None)
            is_favorite = payload.get('isFavorite', None)
            book_id = payload.get('bookId', None)

            if username and is_favorite is not None and book_id:
                user = get_object_or_404(CustomUser, username=username)
                numbers = user.get_numbers()

                if is_favorite:
                    numbers.append(int(book_id))
                else:
                    numbers.remove(int(book_id))

                user.set_numbers(numbers)
                user.save()

                return JsonResponse({'Mensaje': 'Favorito actualizado satisfactoriamente.'})
            else:
                return JsonResponse({'error': 'Campos faltantes o inválidos.'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Solicitud inválida: JSON mal formado.'}, status=400)

class FavoriteBooks(APIView):
    def get(self, request):
        # Obtener el usuario actual
        user = request.user

        # Obtener los IDs de los libros favoritos del usuario
        favorite_ids = user.get_numbers()

        # Obtener los libros favoritos según los IDs
        favorite_books = Book.objects.filter(id__in=favorite_ids)

        context = {
            'favorite_books': favorite_books
        }
        print(favorite_books)  
        return render(request, 'siteapp/favorite_books.html', context)


class RemoveFavorite(APIView):
    def post(self, request, book_id):
        # Obtener el usuario actual
        user = request.user

        # Obtener los IDs de los libros favoritos del usuario
        favorite_ids = user.get_numbers()

        # Verificar si el libro está en la lista de favoritos del usuario
        if book_id in favorite_ids:
            # Eliminar el ID del libro de la lista de favoritos
            favorite_ids.remove(book_id)

            # Actualizar los números en el campo "numbers" del usuario
            user.set_numbers(favorite_ids)
            user.save()

        return redirect('favorite_books')
    
class CheckFavorite(APIView):
    def get(self, request, username, book_id):
        try:
            user = get_object_or_404(CustomUser, username=username)
            numbers = user.get_numbers()
            is_favorite = int(book_id) in numbers
            return Response({'isFavorite': is_favorite})
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        
class CommentCreateView(APIView):
    def post(self, request):
        username = request.data.get('username')
        book_id = request.data.get('bookId')
        calificacion = request.data.get('rating')
        comentario = request.data.get('comment')

        try:
            # Obtener el usuario relacionado con el username
            user = get_object_or_404(CustomUser, username=username)

            # Crear un nuevo comentario
            comment = Comment.objects.create(user=user, libro_id=book_id, calificacion=calificacion, comentario=comentario)

            # Serializar los datos del comentario creado
            serializer = CommentSerializer(comment)

            return Response(serializer.data)

        except CustomUser.DoesNotExist:
            return Response({'error': 'El usuario no existe'}, status=400)

        except Exception as e:
            return Response({'error': str(e)}, status=500)

        
class CommentListView(APIView):
    def get(self, request, book_id):
        try:
            comments = Comment.objects.filter(libro_id=book_id)
            serializer = CommentSerializerGet(comments, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        

class CommentUpdateView(APIView):
    def put(self, request, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            return Response({'error': 'El comentario no existe'}, status=404)
        
        # Actualizar los campos del comentario
        comment.comentario = request.data.get('comentario', comment.comentario)
        comment.calificacion = request.data.get('calificacion', comment.calificacion)
        comment.save()
        
        # Serializar los datos del comentario actualizado
        serializer = CommentSerializer(comment)
        
        return Response(serializer.data)

class CommentDeleteAPIView(APIView):
    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response({'message': 'Comentario eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)