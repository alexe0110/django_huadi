from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Comment


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'articles/list.html', {'latest_article_list': latest_article_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")
    return render(request, 'articles/detail.html', {'article': a})


def leave_comment(request, article_id):
    pass


def test(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Тест</title>
        </head>
        <body>
            <h1>Это тетовая старница</h1>
            <h3>Проверка</h3>
        </body>
        </html>
    """)
