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


class NewsByCategoryView(ListView):
    model = News
    template_name = 'home/categoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoryName = self.kwargs['category']
        print(categoryName)
        print(categoryName)
        print(categoryName)
        print(categoryName)
        #newsByCategory = News.objects.filter(category__name=categoryName)
        context['news_selection'] = News.objects.filter(category__name = categoryName)
        return context

