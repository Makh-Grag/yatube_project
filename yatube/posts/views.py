from multiprocessing import context
from django.shortcuts import render
from .models import Post, Group
from django.shortcuts import get_object_or_404 

#Главная страница
def index(request):   
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим 
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.ojects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group' : group,
        'posts' : posts,
    }
    return render(request, 'posts/group_list.html', context)
