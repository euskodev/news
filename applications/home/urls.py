from os import name 
from django.urls  import include,path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.HomePageView.as_view(),name='home',),
    #path('news_detail', views.HomePageView.as_view(),name='home',),
    path('home/articulo/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail' 
),
    path('newsByFilter/<str:category>/', views.NewsByCategoryView.as_view(), name='newsByQuestion'),

    path('Politicas_de_privacidad',
        views.PoliticasdeprivacidadView.as_view(),
        name='Politicas_de_privacidad',
    ),

        path('Politicas_de_cookies',
        views.PoliticasdecookiesView.as_view(),
        name='Politicas_de_cookies',
    ),

    path('Aviso_legal',
        views.AvisolegalView.as_view(),
        name='Aviso_legal',
    ),


]