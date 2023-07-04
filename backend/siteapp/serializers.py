from rest_framework import serializers
from .models import Book,Categorys, BookStore,Store
from users.models import CustomUser, Comment



class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        fields = ('id','name')

class BookSerializer(serializers.ModelSerializer):
    categorys = BookCategorySerializer()
    class Meta:
        model = Book
        fields = ('id', 'title','categorys','image','editorial','autor','calificacion')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name',)

class StoreBookSerializer(serializers.ModelSerializer):
    store =  StoreSerializer()
    class Meta:
        model = BookStore
        fields = ('price','discount','stock','store')        

class BookListCategorySerializer(serializers.ModelSerializer):
    categorys = BookCategorySerializer()
    class Meta:
        model = Book
        fields = ('id', 'title','image','editorial','autor','isbn','reseña','sub_category','formato','idioma','pagina','calificacion','categorys')
        
class BookListCategorySerializer1(serializers.ModelSerializer):
    categorys = BookCategorySerializer()
    bookStore = StoreBookSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title','image','editorial','autor','isbn','reseña','sub_category','formato','idioma','pagina','calificacion','categorys','bookStore')

class PaginationsSerializers(serializers.Serializer):
    count = serializers.IntegerField()
    books = BookListCategorySerializer(many= True)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comentario', 'calificacion', 'libro_id']

class CommentSerializerGet(serializers.ModelSerializer):
    user_image = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username')
    comment_id = serializers.IntegerField(source='id')  # Agregar el campo "comment_id"

    class Meta:
        model = Comment
        fields = ['comment_id', 'username', 'comentario', 'calificacion', 'user_image', 'libro_id']

    def get_user_image(self, obj):
        if obj.user.image:
            return obj.user.image.url
        return None
