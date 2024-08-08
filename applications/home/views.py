from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)
from .models import News

# Create your views here.
class HomePageView(ListView):
    model = News
    template_name = "home/index.html"
    context_object_name = 'news_selection'
    ordering = [
        '-date_time'
    ]

class NewsView(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news_selection'
    ordering = [
        '-date_time'
    ]

class NewsDetailView(DetailView):
    model = News # Especifica el modelo Blog
    template_name = 'home/detalle_noticia.html' # Define el template "articulo_completo.html"
    context_object_name = 'news_detail'
