from django import forms
from users.models import CustomUser
from .models import Article, ArticleSeries
from tinymce.widgets import TinyMCE

class SeriesCreateForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=CustomUser.objects.all())

    class Meta:
        model = ArticleSeries

        fields = [
            'title',
            'subtitle',
            'slug',
            'image',
            'author',
        ]
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'slug': 'Identificador URL',
            'image': 'Imagen',
            'author': 'Autor',
        }

class ArticleCreateForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=CustomUser.objects.all())

    class Meta:
        model = Article

        fields = [
            'title',
            'subtitle',
            'article_slug',
            'content',
            'notes',
            'series',
            'image',
            'author',
        ]
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'image': 'Imagen',
            'article_slug': 'Identificador URL del artículo',
            'content': 'Contenido',
            'notes': 'Notas',
            'series': 'Serie',
            'image': 'Imagen',
            'author': 'Autor',
        }
class SeriesUpdateForm(forms.ModelForm):
    class Meta:
        model = ArticleSeries

        fields = [
            'title',
            'subtitle',
            'image',
        ]
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'image': 'Imagen',
        }

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = [
            'title',
            'subtitle',
            'content',
            'notes',
            'series',
            'image',
        ]
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'content': 'Contenido',
            'notes': 'Notas',
            'series': 'Serie',
            'image': 'Imagen',
        }
        

class NewsletterForm(forms.Form):
    subject = forms.CharField(label="Tema")
    message = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Contenido del email")
    send_to_all = forms.BooleanField(label="Enviar a todos los usuarios", required=False)
    receivers = forms.CharField(label="Destinatarios", required=False)

    def clean(self):
        cleaned_data = super().clean()
        send_to_all = cleaned_data.get('send_to_all')
        receivers = cleaned_data.get('receivers')

        if not send_to_all and not receivers:
            raise forms.ValidationError("Debes seleccionar destinatarios específicos o marcar 'Enviar a todos los usuarios'.")

        return cleaned_data
