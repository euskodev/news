from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from datetime import datetime


# Se obtiene el modelo de usuario de Django
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        """Devuelve el título del post como representación en cadena."""
        return self.name

    def get_summary(self):
        """Devuelve un resumen del cuerpo del post (primeras 200 palabras)."""
        return self.content[:200]


class News(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField( blank=True,null=True)
    summary = HTMLField( blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True)
    highlight1 = models.BooleanField(blank=True,null=True)
    highlight2 = models.BooleanField(blank=True,null=True)
    highlight3 = models.BooleanField(blank=True,null=True)
    recent_post1 = models.BooleanField(blank=True,null=True)
    recent_post2 = models.BooleanField(blank=True,null=True)
    recent_post3 = models.BooleanField(blank=True,null=True)

    def __str__(self):
        """Devuelve el título del post como representación en cadena."""
        return self.title

    def get_summary(self):
        """Devuelve un resumen del cuerpo del post (primeras 200 palabras)."""
        return self.content[:200]
    

class Comment(models.Model):
    comment=models.TextField(blank=True,null=True)
    news=models.ForeignKey(News, on_delete=models.CASCADE, blank=True, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name=models.CharField(max_length=40, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

