from django.shortcuts import render
from django.http.response import JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views import generic
from .models import Shopping
from .serializers import ShoppingSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def article_list(request):
    # get list of articles, Post new articles
    if request.method == 'GET':
        articles = Shopping.objects.all()

        article_name = request.GET.get('article_name', None)
        if article_name is not None:
            articles = articles.filter(article_name__icontains=article_name)

        article_serializer = ShoppingSerializer(articles, many=True)
        return JsonResponse(article_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        article_data = JSONParser().parse(request)
        article_serializer = ShoppingSerializer(data=article_data)
        if article_serializer.is_valid():
            article_serializer.save()
            return JsonResponse(article_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    # find article by id
    try:
        article = Shopping.objects.get(pk=pk)
    except Shopping.DoesNotExist:
        return JsonResponse({'message': 'The article does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        article_serializer = ShoppingSerializer(article)
        return JsonResponse(article_serializer.data)
    elif request.method == 'PUT':
        article_data = JSONParser().parse(request)
        article_serializer = ShoppingSerializer(article, data=article_data)
        if article_serializer.is_valid():
            article_serializer.save()
            return JsonResponse(article_serializer.data)
        return JsonResponse(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return JsonResponse({'message': 'Article was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_articles = Shopping.objects.all().count()
    # Available bio articles
    num_articles_bio = Shopping.objects.filter(bio__exact=True).count()

    context = {
        'num_articles': num_articles,
        'num_instances': num_articles_bio,

    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class ArticlesListView(generic.ListView):
    model = Shopping
    context_object_name = 'articles_list'  # your own name for the list as a template variable
    # queryset = Shopping.objects.filter(category__icontains='Wurst')[:5]  # Get 5 books containing the category Wurst
    template_name = 'shopping/templates/articles_list.html'  # Specify your own template name/location


class ArticleDetailView(generic.DetailView):
    model = Shopping
    context_object_name = 'article'
    def book_detail_view(request, primary_key):
        try:
            article = Shopping.objects.get(pk=primary_key)
            print(primary_key)
        except Shopping.DoesNotExist:
            raise Http404('Article does not exist')

        return render(request, 'shopping/templates/article_detail.html', context={'article': article})