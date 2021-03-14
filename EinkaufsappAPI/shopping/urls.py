from django.urls import path
from . import views

urlpatterns = [
    #url(r'^api/articles$', article_list),
    #url(r'^api/articles/(?P<pk>[0-9]+)$', article_detail),
    path('', views.index, name='index'),
    path('articles/', views.ArticlesListView.as_view(template_name='articles_list.html'), name='articles_list'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(template_name='article_detail.html'),
         name='article_detail'),
]

