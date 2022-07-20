from django.http import HttpResponse
from django.shortcuts import render

#Главная страница
def index(request):    
    template = 'posts/index.html'
    return render(request, template) 

# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    return HttpResponse(f'Группированные посты по запросу {slug}')
