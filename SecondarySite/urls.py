from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('Categories/<int:cate_id>/', views.Categories),

]
