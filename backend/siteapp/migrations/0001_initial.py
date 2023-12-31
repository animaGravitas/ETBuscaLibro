# Generated by Django 4.2.1 on 2023-07-04 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(default=None, null=None, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('image', models.URLField(blank=True, default=None, max_length=300, null=True)),
                ('editorial', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('autor', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('isbn', models.BigIntegerField(blank=True, default=None, help_text='codigo del libro', null=True)),
                ('reseña', models.TextField(blank=True, default=None, null=True)),
                ('sub_category', models.CharField(blank=True, default=None, max_length=40, null=True, verbose_name='sub-Categoria')),
                ('formato', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('idioma', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('pagina', models.IntegerField(blank=True, default=None, null=True)),
                ('calificacion', models.CharField(blank=True, default=0, help_text='rating: 5', max_length=200, null=True, verbose_name='rating')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('web', models.URLField(max_length=400, verbose_name='web store')),
                ('image', models.URLField(blank=True, default=None, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
                'db_table': 'store',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_platform_id', models.CharField(default=None, max_length=20, null=True, verbose_name='Id comentario en plataforma')),
                ('name', models.CharField(max_length=300)),
                ('image_url', models.URLField(blank=True, default='https://cdn-icons-png.flaticon.com/512/6378/6378141.png', null=True, verbose_name='Imagen Medium')),
                ('description', models.TextField()),
                ('rating', models.CharField(max_length=300, verbose_name='evaluacion del curso')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteapp.book')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteapp.store')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='CategorysScraper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('category', models.ForeignKey(default=None, help_text='my category', null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteapp.categorys')),
                ('store', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteapp.store')),
            ],
            options={
                'verbose_name': 'Category Scraper',
                'verbose_name_plural': 'Category Scraper',
                'db_table': 'category scraper',
            },
        ),
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_book', models.URLField(default='', max_length=400, verbose_name='url book')),
                ('price', models.FloatField(blank=True, default=None, null=True, verbose_name='Precio del libro')),
                ('discount', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='descuento del libro')),
                ('stock', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='stock libro en la tienda')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteapp.book')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteapp.store')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='categorys',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteapp.categorys'),
        ),
    ]
