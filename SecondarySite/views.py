from django.shortcuts import render
from django.http import HttpResponse
from SecondarySite.models import Announcement

def index(request):
    return HttpResponse("Вы на главной страницеtttttttttttttttttt")


def Categories(request, cate_id):
    return HttpResponse(f"<h1>Статьи по Категориям</h1><p>id: {cate_id}</p>")