from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница социальной сети.')

# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    return HttpResponse(f'Группированные посты по запросу {slug}')
