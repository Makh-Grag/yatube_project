from django.http import HttpResponse
from django.shortcuts import render

#Главная страница
def index(request):    
    template = 'posts/index.html'
    title = "YaTube"
    text = "Это главная страница проекта YaTube"
    # Словарь
    context = {
        'title' : title,
        'text': text
}
    return render(request, template, context) 

def group_posts(request):
    template = 'posts/group_list.html'
    title = "YaTube"
    text = "Здесь будет информация о группах проекта Yatube"
    context = {
        'title' : title,
        'text': text
    }
    return render(request, template, context)
