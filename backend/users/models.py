from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
import os

# Create your models here.
class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Users", self.username, instance)
        return None

    STATUS = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = models.TextField("Description", max_length=600, default='', blank=True)
    image = models.ImageField(default='default/user.png', upload_to=image_upload_to)
    numbers = models.CharField(max_length=255, blank=True) 

    def get_numbers(self):
        numbers_str = self.numbers or ''  # Si self.numbers es None, se asigna una cadena vacía
        numbers_int = [int(num) for num in numbers_str.split(',') if num]  # Se omiten las cadenas vacías
        return numbers_int

    def set_numbers(self, numbers):
        numbers_str = [str(num) for num in numbers]
        self.numbers = ','.join(numbers_str)

    def __str__(self):
        return self.username
    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, related_name='comments', on_delete=models.CASCADE)
    libro_id = models.IntegerField(blank=True, null=True)
    calificacion = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True)

    def __str__(self):
        return f"Comment by {self.user.username}"
    
class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
    

