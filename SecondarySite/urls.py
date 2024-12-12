from django.urls import path, re_path, register_converter
from . import views
from . import converter

register_converter(converter.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index), # http://127.0.0.1:8000
    path('cate/<int:cate_id>/', views.Categories), # http://127.0.0.1:8000/cate/'3/' (Важно! слаг более общий и может перекрыть этот путь так что лучше слаг ставить после)
    path('cate/<slug:cate_slug>/', views.Categories_by_slug), # http://127.0.0.1:8000/cate/'ss9/'
    path("archive/<year4:year>/", views.Archive),

    # path('badrequest/', views.bad_request),
    # path('for-request/', views.forbidden_page),
    # path('found-request/', views.page_not_found),
    # path('ser-request/', views.server_error)

]
