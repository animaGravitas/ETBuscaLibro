from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet, BookDetailView, BookCategory,IsAuthenticatedView, BookCategoryView, BookListCategory, ListCategoryMundoComic, ListCategoryComputacionInformatica, ListCategoryLiteratura
from .views import ListCategoryInfantil, ListCategoryNovedades, ListCategoryvendidos,ListCategoryciencias,SearchBoook, favorite, FavoriteBooks, RemoveFavorite, CheckFavorite, CommentCreateView, CommentListView, CommentUpdateView, CommentDeleteAPIView
router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'books-category', BookCategory)
router.register(r'list_book', BookListCategory)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path(r'book-detail/<book_id>', BookDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('category/<category>', BookCategoryView.as_view()),
    path('category-mundo-Comic/', ListCategoryMundoComic.as_view()),
    path('category-computacion-informatica/',
         ListCategoryComputacionInformatica.as_view()),
    path('category-literatura/',
         ListCategoryLiteratura.as_view()),
    path('category-infantil/',
         ListCategoryInfantil.as_view()),
    path('category-vendidos/',
         ListCategoryvendidos.as_view()),
    path('category-ciencias/',
         ListCategoryciencias.as_view()),
    
     path('category-novedades/',
         ListCategoryNovedades.as_view()),
     
     path('search/',SearchBoook.as_view()),

     path('is_authenticated/',IsAuthenticatedView.as_view(), name='is_authenticated'),

     path('favorite/',favorite.as_view(), name='favorite'),

     path('favorite-books/', FavoriteBooks.as_view(), name='favorite_books'),
     path('remove-favorite/<int:book_id>/', RemoveFavorite.as_view(), name='remove_favorite'),
     path('check-favorite/<str:username>/<int:book_id>/', CheckFavorite.as_view(), name='check_favorite'),
     path('comment-create/', CommentCreateView.as_view(), name='comment-create'),
     path('comments/<int:book_id>/', CommentListView.as_view(), name='comment-list'),
     path('comment-update/<int:comment_id>/', CommentUpdateView.as_view(), name='comment-update'),
     path('comment-delete/<int:pk>/', CommentDeleteAPIView.as_view(), name='comment-delete'),
]
