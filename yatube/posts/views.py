from argparse import REMAINDER
from cgitb import text
from multiprocessing import context
from re import template
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

#Главная страница
def index(request):    
    template = 'posts/index.html'
    title = "Yatube"
    text = "Это главная страница проекта Yatube"
    context = {
        # В словарь можно передать переменную
        'title' : title,
        'text': text,
    }
    return render(request, template, context) 

def group_posts(request):
    template = 'posts/group_list.html'
    title = "YaTube"
    text = "Здесь будет информация о группах проекта Yatube"
    context = {
        'title' : title,
        'text': text,
    }
    return render(request, template, context)
