from django.shortcuts import render
from django.http import HttpResponse
from SecondarySite.models import Announcement

def index(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Announcement.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
        return HttpResponse(s, content_type='text/plain; charset=utf-8')