from django.urls import path
from .views import *




urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>', category_page, name='category'),
    path('article/<int:article_id>', article_detail, name='article'),
]

