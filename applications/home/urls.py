from os import name 
from django.urls  import include,path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.HomePageView.as_view(),name='home',),
    #path('news_detail', views.HomePageView.as_view(),name='home',),
    path('home/articulo/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail' 
),
]