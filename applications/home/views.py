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

    #q = ProductOrder.objects.values('Category').distinct()

class NewsView(ListView):
    model = News
    template_name = 'home/index.html'
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
        context['news_selection'] = News.objects.filter(category__name = categoryName).order_by('-id')
        return context

class PoliticasdeprivacidadView(TemplateView):
    template_name = "home/Politicas_de_privacidad.html"

class PoliticasdecookiesView(TemplateView):
    template_name = "home/Politicas_de_cookies.html"


class AvisolegalView(TemplateView):
    template_name = "home/Aviso_legal.html"

class Error404View(TemplateView):
  template_name = "home/error-404.html"

def custom_404(request, exception):
    return render(request, 'home/erro-404.html', status=404)


