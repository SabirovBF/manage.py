from django.shortcuts import render


from . import models


def index(request):
    news = models.News.objects.all()
    categories = models.Category.objects.all()
    context = {'news': news,
               'categories': categories,
               'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context=context)

def get_category(request, category_id):
    news = models.News.objects.filter(category=category_id)
    categories = models.Category.objects.all()
    category = models.Category.objects.get(pk=category_id)
    context = {'news': news,
               'categories': categories,
               'category': category,
               }
    return render(request, 'news/category.html', context=context)
