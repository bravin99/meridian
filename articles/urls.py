from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='articles'),
    path('tutorial/<slug:year>/<slug:month>/<slug:day>/<slug:author>/<slug:slug>/',
         views.ArticleDetailView.as_view(), name='article_detail'),
    path('favourites/<slug:slug>/', views.favourite_articles, name='favourites'),
    path('search/', views.ArticleSearchView.as_view(), name='search'),
    path('tags/<slug:tag_slug>/', views.tagged, name='tagged'),    
]