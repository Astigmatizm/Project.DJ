from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseBadRequest, \
    HttpResponseForbidden


def index(request):
    return HttpResponse("Страница работает!")

def Categories(request, cate_id):
    return HttpResponse(f"<h2>Статья по категориям!</h2><p>id: {cate_id}</p>")

def Categories_by_slug(request, cate_slug):
    return HttpResponse(f"<h2>Статья по категориям!</h2><p>slug: {cate_slug}</p>")

def Archive(request, year):
    if year > 2024:
        raise Http404("не найденно")

    return HttpResponse(f"<h2>Архив по годам</h2><p>slug: {year}</p>")

def bad_request(request, exception):    # error400
    return HttpResponseBadRequest('<h1>error 400. Некорректный Запрос</h1>')

def forbidden_page(request, exception):     # error403
    return HttpResponseForbidden('<h1>error 403. Доступ запрещен</h1>')

def page_not_found(request, exception):     # error404
    return HttpResponseNotFound("<h1>error 404. Страница не найдена</h1>")

def server_error(request):     # error500
    return HttpResponseServerError('<h1>error 500. Внутренняя ошибка сервера</h1>')