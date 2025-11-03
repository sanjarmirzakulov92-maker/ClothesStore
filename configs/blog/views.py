from django.shortcuts import render
from .models import *


def index(request):
    categories= Category.objects.all()
    articles = Article.objects.all()

    context = {
        'title': 'Home',
        'categories': categories,
        'articles': articles
    }


    return render(request, 'blog/index.html', context)


def category_page(request, category_id):
    categories = Category.objects.all()
    articles = Article.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    context = {
        'title': f'{category.title}',
        'categories': categories,
        'articles': articles
    }
    return render(request, 'blog/index.html', context)

def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)


    context = {
        'title': f'{article.title}',
        'article': article,
    }

    return render(request, 'blog/article_detail.html', context)
